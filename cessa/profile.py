#!/usr/bin/env python
# encoding: utf-8

"""
cessa.profile
=============

This module implements the basic operations of seccomp profile.

:Copyright (c) 2017 by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

class Seccomp(object):

    """ Represents the config for a seccomp profile for syscall restriction.

    """

    def __init__(self, action):
        self.default_action = action
        self.architectures = []
        self.arch_map = []
        self.syscalls = []

    def
