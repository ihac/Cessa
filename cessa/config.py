# encoding: utf-8

"""
cessa.config
===========

This module defines all configuration constants for seccomp profile.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

class Action(object):

    """Defines actions for seccomp rules

    """
    KILL  = 'SCMP_ACT_KILL'
    TRAP  = 'SCMP_ACT_TRAP'
    ERRNO = 'SCMP_ACT_ERRNO'
    TRACE = 'SCMP_ACT_TRACE'
    ALLOW = 'SCMP_ACT_ALLOW'

class Arch(object):

    """Defines architectures

    """
    X86         = 'SCMP_ARCH_X86'
    X86_64      = 'SCMP_ARCH_X86_64'
    X32         = 'SCMP_ARCH_X32'
    ARM         = 'SCMP_ARCH_ARM'
    AARCH64     = 'SCMP_ARCH_AARCH64'
    MIPS        = 'SCMP_ARCH_MIPS'
    MIPS64      = 'SCMP_ARCH_MIPS64'
    MIPS64N32   = 'SCMP_ARCH_MIPS64N32'
    MIPSEL      = 'SCMP_ARCH_MIPSEL'
    MIPSEL64    = '_ARCH_MIPSEL64'
    MIPSEL64N32 = '_ARCH_MIPSEL64N32'
    PPC         = '_ARCH_PPC'
    PPC64       = '_ARCH_PPC64'
    PPC64LE     = '_ARCH_PPC64LE'
    S390        = '_ARCH_S390'
    S390X       = '_ARCH_S390X'

class Operator(object):

    """Defines operators for syscall arguments

    """
    NOT_EQUAL     = 'SCMP_CMP_NE'
    LESS_THAN     = 'SCMP_CMP_LT'
    LESS_EQUAL    = 'SCMP_CMP_LE'
    EQUAL_TO      = 'SCMP_CMP_EQ'
    GREATER_EQUAL = 'SCMP_CMP_GE'
    GREATER_THAN  = 'SCMP_CMP_GT'
    MASKED_EQUAL  = 'SCMP_MASKED_EQ'
