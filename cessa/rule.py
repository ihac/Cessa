#!/usr/bin/env python
# encoding: utf-8

"""
cessa.rule
==========

This module implements limit rule class and corresponding interfaces.

: Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

import os
import re
import knowledge

from cessa.config import Action, Operator
from cessa.knowledge import es_engine
from pyke import goal

class Rule(object):

    """ Represents a seccomp limit rule

    """

    def __init__(self, syscall, action):
        if action not in Action:
            raise ValueError('Action \'{}\' is unsupported or illegal. Use action in config.Action instead'.format(action))
        self.name = syscall
        self.action = action
        self.args = []
        self.omit = False

    def __str__(self):
        output = 'Syscall {}'.format(self.syscall)
        action_str = {
            Action.KILL: 'will be KILLed',
            Action.TRAP: 'will be TRAPed',
            Action.ERRNO: 'will be ERRNOed',
            Action.TRACE: 'will be TRACEd',
            Action.ALLOW: 'will be ALLOWed'
        }.get(self.action, None)
        output += '{} when '.format(action_str)

        num = len(self.args)
        for i in range(num):
            output += '{} and '.format(self.args[i]) if i < num - 1 else '{}.'.format(self.args[i])
        return output

    def add_condition(self, cond):
        """ adds argument condition.

        :cond: argument condition
        :returns: None

        """
        # Be sure that at most one condition per argument is allowed for now.
        if len(self.args) != 0:
            for arg in self.args:
                if arg.index == cond.index:
                    raise ValueError('Unable to add multiple conditions based on the same argument owing to the limitation of libseccomp')
        self.args.append(cond)


class Condition(object):

    """ Represents an argument condition

    """
    def __init__(self, index, op, value, value2=None):
        if index > 5:
            raise ValueError('At most 6 arguments is supported')
        if op not in Operator:
            raise ValueError('Operator \'{}\' is unsupported or illegal. Use operator in config.Operator instead'.format(op))
        if type(value) != int or (value2 != None and type(value2) != int):
            raise ValueError('Only integer value is allowed owing to the limitation of libseccomp')
        if op == Operator.MASKED_EQUAL and value2 == None:
            raise ValueError('Two value is required for operation MASKED_EQUAL')

        self.index = index
        self.operator = op
        self.value = value
        self.value2 = value2 if op == Operator.MASKED_EQUAL else None

    def __str__(self):
        index_str = {
            0: '0th',
            1: '1st',
            2: '2nd',
            3: '3rd',
            4: '4th',
            5: '5th'
        }.get(self.index, None)
        op_str = {
            Operator.NOT_EQUAL: 'is not equal to',
            Operator.LESS_THAN: 'is less than',
            Operator.LESS_EQUAL: 'is less than or equal to',
            Operator.EQUAL_TO: 'is equal to',
            Operator.GREATER_EQUAL: 'is greater than or equal to',
            Operator.GREATER_THAN: 'is greater than',
            Operator.MASKED_EQUAL: 'is masked equal to',
        }.get(self.operator, None)
        value_str = str(self.value) if self.value2 == None else '{} with {}'.format(self.value, self.value2)

        return '{} argument {} {}'.format(index_str, op_str, value_str)

def gen_rules(syscall_list, record_dir, ctype_file, level='easy'):
    """ generates limit rules according to the preprocessed syscall trace records.

    :syscall_list: list of syscall names
    :record_dir: directory where program stores the preprocessed trace records.
    :level: limit level of rules
    :returns: TODO

    """
    if not os.path.isdir(record_dir):
        raise ValueError('\'{}\' is not a directory'.format(record_dir))
    gen_rules_f = {
        'easy': gen_easy_rules,
        'normal': gen_normal_rules,
        'hard': gen_hard_rules,
        'custom': gen_custom_rules
    }.get(level, None);
    if gen_rules_f == None:
        raise ValueError('\'{}\' is not a legal level'.format(level))
    return gen_rules_f(syscall_list, record_dir, ctype_file)

def _retrieve_arg_value(syscall, arg_record_file):
    """ retrieves argument values from a preprocessed record file

    :syscall: the name of system call
    :arg_record_file: output file of data_preprocessing()
    :returns: dictionary with key=combination of syscall name and arg name, value=set of arg value

    """
    arg_value_dict = {}
    for line in open(arg_record_file, 'r'):
        _, *arg_list = line.split()
        for arg in arg_list:
            p = re.match("(\w+)=(\d+)\(.*)", arg)
            if p == None:
                continue
            arg_name, arg_value = syscall+'_'+p.group(1), int(p.group(2))
            if arg_value_dict.get(arg_name, None) == None:
                arg_value_dict[arg_name] = {arg_value}
            else:
                arg_value_dict[arg_name].add(arg_value)
    return arg_value_dict

def gen_easy_rules(syscall_list, *unused):
    return [Rule(syscall, Action.ALLOW) for syscall in syscall_list]

def gen_normal_rules(syscall_list, record_dir, *unused):
    rule_list = []
    for syscall in syscall_list:
        syscall_dir = os.path.join(record_dir, syscall)
        if not os.path.isdir(syscall_dir):
            raise RuntimeError('\'{}\' is not a directory'.format(syscall_dir))
        rule = Rule(syscall, Action.ALLOW)
        try:
            #  ctype_list = knowledge.load_ctype(ctype_file)
            arg_value_dict = _retrieve_arg_value(syscall, os.path.join(syscall_dir, 'args.uniq.list'))
            for arg_name, arg_value_set = arg_value_dict.items():
                arg_type = knowledge.get_arg_type(arg_name)
                arg_index = knowledge.get_index(arg_name)
                if arg_type == 'pointer' or arg_type == 'no_range':
                    continue
                if arg_type == 'range':
                    all_value_range = knowledge.get_value_range(arg_name)
                    if len(arg_value_set) <= 5:
                        for value in arg_value_set:
                            rule = Rule(syscall, Action.ALLOW)
                            rule.add_condition(Condition(arg_index, Operator.EQUAL_TO, value))
                            rule_list.append(rule)
                    elif len(arg_value_set) >= len(all_value_range) - 5:
                        for value in all_value_range:
                            if value in arg_value_set:
                                continue
                            rule = Rule(syscall, Action.ALLOW)
                            rule.add_condition(Condition(arg_index, Operator.NOT_EQUAL, value))
                            rule_list.append(rule)
                #  if len(arg_value_set) <= 5:
                elif
        except Exception as e:
            raise e
        rule_list.append(rule)
    return rule_list

def gen_hard_rules(syscall_list, record_dir, ctype_file):
    pass

def gen_custom_rules(syscall_list, record_dir, *unused):
    """ generates limit rules by asking user a set of questions

    :syscall_list: TODO
    :record_dir: TODO
    :*unused: TODO
    :returns: TODO

    """
    pass
