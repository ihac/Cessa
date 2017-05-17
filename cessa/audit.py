#!/usr/bin/env python3
# encoding: utf-8

"""
cessa.audit
===========

This module implements interfaces for testing seccomp profile and auditing container.

:Copyright (c) by hac(Xiao An) <hac@zju.edu.cn>. All Rights Reserved.

"""

import re
import time
from cessa.rule import gen_rules
from cessa.profile import dump_rules
from cessa.config import Level
LOG_FILE = '/var/log/audit/audit.log'
SYSTABLE_FILE = 'expert/systable.list'

def _get_seccomp_events(start_time):
    """ gets seccomp events from auditd log file

    :start_time: only seccomp events after start_time will be returned
    :returns: seccomp events list(returned raw, without formatting)

    """
    #TODO logfile path
    events = []
    for line in reversed(list(open(LOG_FILE, 'r'))):
        item1, item2 = line.split()[0:2]
        _, event_type = item1.split('=')
        p = re.match("msg=audit\((.*):\d+\).*", item2)
        time = float(p.group(1))
        if time > start_time and event_type == 'SECCOMP':
            events.append(line)
        elif time < start_time:
            break
    return events

def load_systable(systable_file):
    """ loads syscall table from file

    :systable_file: file contains syscall table
    :returns: syscall table(dictionary)

    """
    systable = {}
    try:
        with open(systable_file, 'r') as f:
            for line in f:
                sys_id, sys_name = line.split()[0:2]
                systable[int(sys_id)] = sys_name
    except:
        raise RuntimeError('Unable to load syscall table from \'{}\''.format(systable_file))
    return systable



def syscall_name(systable, syscall_id):
    """ gets syscall name from syscall id

    :syscall_id: syscall id
    :returns: syscall name

    """
    return systable.get(syscall_id, '')

def adjust_seccomp(container):
    """ adjusts seccomp filter rules by testing container

    :container: Container object
    :rule_list: rule list generated by gen_rules()
    :returns: container

    """
    if container.seccomp == None:
        raise ValueError('No seccomp profile is specified for container \'{}\''.format(container.name))
    if container.workload == None:
        raise ValueError('No workload script is specified for container \{}\''.format(container.name))

    systable = load_systable(SYSTABLE_FILE)
    while True:
        # test
        start_time = time.time()
        container.run(with_seccomp=True)
        container.exec_workload()
        container.remove()

        # audit
        events = _get_seccomp_events(start_time)
        if len(events) == 0:
            break
        # make sure no duplicate rules generated
        error_syscall_set = set()
        for event in reversed(events):
            p = re.match(".*syscall=(\d+).*", event)
            if p != None:
                error_syscall_set.add(int(p.group(1)))
        for sys_id in error_syscall_set:
            sys_name = syscall_name(systable, sys_id)
            print('adjust \'{}\' to lower limit level'.format(sys_name))
            container.del_rules(sys_name)
            container.add_rules(gen_rules([sys_name], level=Level.NAME))
        # replace original seccomp profiles with new rules
        dump_rules(container.seccomp, container.rules)
