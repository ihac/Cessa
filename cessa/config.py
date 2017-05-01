# encoding: utf-8

"""
cessa.config
===========

This module defines all configuration constants for seccomp profile.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

from enum import Enum

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

