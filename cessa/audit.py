#!/usr/bin/env python3
# encoding: utf-8

"""
cessa.audit
===========

This module implements interfaces for testing seccomp profile and auditing container.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

import re

def get_seccomp_events(start_time):
    """ gets seccomp events from auditd log file

    :start_time: only seccomp events after start_time will be returned
    :returns: seccomp events list(returned raw, without formatting)

    """
    #TODO logfile path
    log_file = '/var/log/audit/audit.log'
    events = []
    for line in reversed(list(open(log_file, 'r'))):
        item1, item2 = line.split()[0:2]
        _, event_type = item1.split('=')
        p = re.match("msg=audit\((.*):\d+\).*", item2)
        time = float(p.group(1))
        if time > start_time and event_type == 'SECCOMP':
            events.append(line)
        elif time < start_time:
            break
    return events
