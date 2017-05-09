# encoding: utf-8

"""
cessa.config
===========

This module defines all configuration constants for seccomp profile.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

from enum import Enum, unique

"""Defines actions for seccomp rules
"""
Action = Enum('Action', ['KILL',
                         'TRAP',
                         'ERRNO',
                         'TRACE',
                         'ALLOW'])

"""Defines architectures
"""
Arch = Enum('Arch', ['X86',
                     'X86_64',
                     'X32',
                     'ARM',
                     'AARCH64',
                     'MIPS',
                     'MIPS64',
                     'MIPS64N32',
                     'MIPSEL',
                     'MIPSEL64',
                     'MIPSEL64N32',
                     'PPC',
                     'PPC64',
                     'PPC64LE',
                     'S390',
                     'S390X'])

"""Defines operators for syscall arguments
"""
Operator = Enum('Operator', ['NOT_EQUAL',
                             'LESS_THAN',
                             'LESS_EQUAL',
                             'EQUAL_TO',
                             'GREATER_EQUAL',
                             'GREATER_THAN',
                             'MASKED_EQUAL'])

@unique
class Level(Enum):

    """ Represents the level of rule generation

    """
    NAME = 1
    ARG = 2
    CTYPE = 3
    CUSTOM = 4

    def __str__(self):
        return 'Level-{}'.format(self.name)

    def degrade(self, num=1):
        new_value = self.value - num > 0
        if new_value < Level.NAME.value:
            new_value = Level.NAME.value
        return Level(new_value)

    def upgrade(self, num=1):
        new_value = self.value + num
        if new_value > Level.CUSTOM.value:
            new_value = Level.CUSTOM.value
        return Level(new_value)



