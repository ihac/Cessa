#!/usr/bin/env python
# encoding: utf-8

"""
cessa.rule
==========

This module implements limit rule class and corresponding interfaces.

: Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

from cessa import config

class Rule(object):

    """ Represents a seccomp limit rule

    """

    def __init__(self, syscall, action):
        if action not in config.Action:
            raise ValueError('Action \'{}\' is unsupported or illegal. Use action in config.Action instead'.format(action))
        self.name = syscall
        self.action = action
        self.args = []

    def __str__(self):
        output = 'Syscall {}'.format(self.syscall)

        action_str = {
            config.Action.KILL: 'will be KILLed',
            config.Action.TRAP: 'will be TRAPed',
            config.Action.ERRNO: 'will be ERRNOed',
            config.Action.TRACE: 'will be TRACEd',
            config.Action.ALLOW: 'will be ALLOWed'
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
        if op not in config.Operator:
            raise ValueError('Operator \'{}\' is unsupported or illegal. Use operator in config.Operator instead'.format(op))
        if type(value) != int or (value2 != None and type(value2) != int):
            raise ValueError('Only integer value is allowed owing to the limitation of libseccomp')
        if op == config.Operator.MASKED_EQUAL and value2 == None:
            raise ValueError('Two value is required for operation MASKED_EQUAL')

        self.index = index
        self.operator = op
        self.value = value
        self.value2 = value2 if op == config.Operator.MASKED_EQUAL else None

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
            config.Operator.NOT_EQUAL: 'is not equal to',
            config.Operator.LESS_THAN: 'is less than',
            config.Operator.LESS_EQUAL: 'is less than or equal to',
            config.Operator.EQUAL_TO: 'is equal to',
            config.Operator.GREATER_EQUAL: 'is greater than or equal to',
            config.Operator.GREATER_THAN: 'is greater than',
            config.Operator.MASKED_EQUAL: 'is masked equal to',
        }.get(self.operator, None)
        value_str = str(self.value) if self.value2 == None else '{} with {}'.format(self.value, self.value2)

        return '{} argument {} {}'.format(index_str, op_str, value_str)

def gen_rules(arg1):
    """TODO: Docstring for gen_rules.

    :arg1: TODO
    :returns: TODO

    """
    pass
