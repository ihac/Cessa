#!/usr/bin/env python
# encoding: utf-8

"""
cessa.rule
==========

This module implements limit rule class and corresponding interfaces.

: Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

import os
import knowledge

from cessa.trace import retrieve_arg_value
from cessa.config import Action, Operator
from functools import partial

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

def _gen_multiple_rules(syscall, action, arg_index, op, value_list):
    """ generates multiple rules(for the same argument and the same operator) automatically

    :syscall: syscall name
    :action: the action towards this rules
    :arg_name: the index of argument
    :op: operator
    :value_list: value list of argument
    :returns: rule list

    """
    rule_list = []
    for value in value_list:
        rule = Rule(syscall, action)
        rule.add_condition(Condition(arg_index, op, value))
        rule_list.append(rule)
    return rule_list

def _gen_rules_range(syscall, arg_name, value_set):
    """ generates rules for arguments with 'range' type

    :syscall: syscall name
    :arg_name: argument name
    :value_set: argument value set recorded by sysdig
    :returns: rule list

    """
    rule_list = []
    arg_index = knowledge.get_index(arg_name)
    gen_f = partial(_gen_multiple_rules, syscall, Action.ALLOW, arg_index)
    if len(value_set) <= 3:
        rule_list += gen_f(Operator.EQUAL_TO, value_set)
    else:
        all_value_range = knowledge.get_value_range(arg_name)
        if len(value_set) >= len(all_value_range) - 3:
            non_value_set = {x for x in all_value_range if x not in value_set}
            rule_list += gen_f(Operator.EQUAL_TO, non_value_set)
        else:
            max_v, min_v = max(value_set), min(value_set)
            smaller_num = len([v for v in all_value_range if v < min_v])
            larger_num = len([v for v in all_value_range if v > max_v])
            if smaller_num > larger_num:
                rule_list += gen_f(Operator.GREATER_EQUAL, {min_v})
            else:
                rule_list += gen_f(Operator.LESS_EQUAL, {max_v})
    return rule_list

def _gen_rules_fd(syscall, arg_name, value_set):
    """ generates rules for arguments with 'fd' type

    :syscall: syscall name
    :arg_name: argument name
    :value_set: argument value set recorded by sysdig
    :returns: rule list

    """
    arg_index = knowledge.get_index(arg_name)
    max_fd = 1 << max(value_set).bit_length()
    return _gen_multiple_rules(syscall, Action.ALLOW, arg_index, Operator.LESS_THAN, {max_fd})

def _gen_rules_bufsize(syscall, arg_name, value_set):
    """ generates rules for arguments with 'buf_size' type

    :syscall: syscall name
    :arg_name: argument name
    :value_set: argument value set recorded by sysdig
    :returns: rule list

    """
    arg_index = knowledge.get_index(arg_name)
    max_size = 1 << max(value_set).bit_length()
    return _gen_multiple_rules(syscall, Action.ALLOW, arg_index, Operator.LESS_THAN, {max_size})

def _gen_rules_bitwise(syscall, arg_name, value_set):
    """ generates rules for arguments with 'buf_size' type

    :syscall: syscall name
    :arg_name: argument name
    :value_set: argument value set recorded by sysdig
    :returns: rule list

    """
    arg_index = knowledge.get_index(arg_name)
    powers = 0;
    for value in value_set:
        all_powers = _powers_of_2(value)
        for x in all_powers:
            powers |= x
    powers ^= int('0xFFFFFFFF', base=16)
    rule = Rule(syscall, Action.ALLOW)
    rule.add_condition(Condition(arg_index, Operator.MASKED_EQUAL, 0, powers))

def _powers_of_2(num):
    powers = []
    i = 1
    while (i <= num):
        if i & num != 0:
            powers.append(i)
        i <<= 1
    return powers

def gen_easy_rules(syscall_list, *unused):
    return [Rule(syscall, Action.ALLOW) for syscall in syscall_list]

def gen_normal_rules(syscall_list, record_dir, *unused):
    rule_list = []
    for syscall in syscall_list:
        syscall_dir = os.path.join(record_dir, syscall)
        if not os.path.isdir(syscall_dir):
            raise RuntimeError('\'{}\' is not a directory'.format(syscall_dir))
        try:
            arg_value_dict = retrieve_arg_value(syscall, os.path.join(syscall_dir, 'args.uniq.list'))
            for arg_name, arg_value_set in arg_value_dict.items():
                arg_type = knowledge.get_arg_type(arg_name)
                if arg_type == 'pointer' or arg_type == 'no_range':
                    continue
                if arg_type == 'range':
                    rule_list += _gen_rules_range(syscall, arg_name, arg_value_set)
                elif arg_type == 'fd':
                    rule_list += _gen_rules_fd(syscall, arg_name, arg_value_set)
                elif arg_type == 'bufsize':
                    rule_list += _gen_rules_bufsize(syscall, arg_name, arg_value_set)
                elif arg_type == 'bitwise':
                    rule_list += _gen_rules_bitwise(syscall, arg_name, arg_value_set)
        except Exception as e:
            raise e
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
