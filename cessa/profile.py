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
        # TODO check whether action is legal
        self.default_action = action
        self.architectures = []
        self.arch_map = []
        self.syscalls = []

    def load_rule(self, rule_list):
        """ loads rule into seccomp profile

        :rule_list: list of rule object
        :returns: None

        """
        pass
