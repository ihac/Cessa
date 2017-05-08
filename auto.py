#!/usr/bin/env python3
# encoding: utf-8

import json
from cessa import trace, rule, profile, audit
from cessa.config import Action , Arch, Operator
workload = '/root/cessa/scripts/nginx-test.workload'
trace_file = '/root/cessa/tmp/nginx.trace.list.2'
record_dir = '/root/cessa/tmp'
seccomp_profile = '/root/cessa/nginx-test.profile'

def auto_test():
    syscall_list = trace.data_preprocessing('tmp/nginx.trace.list', 'tmp')
    rules2 = rule.gen_rules(syscall_list, 'tmp', None, level='normal')
    seccomp = profile.Seccomp(Action.ERRNO)
    seccomp.set_arch([Arch.X86_64])
    seccomp.set_rules(rules2)
    json_profile = seccomp.to_json()
    return json.dumps(json_profile, indent=4, sort_keys=True)

def trace_test():
    container = trace.Container('nginx-test', '1e4e93130f1f')
    container.set_option(['-p', '8080:80'])
    container.set_workload(workload)
    trace.trace_syscall(container, trace_file)
    return container, trace.data_preprocessing(trace_file, record_dir)

def gen_rules_test(syscall_list, level='easy'):
    rule_list = rule.gen_rules(syscall_list, record_dir, None, level)
    return rule_list

def dump_rules_test(rule_list):
    profile.dump_rules(seccomp_profile, rule_list)

def adjust_test(container, rule_list):
    container.set_seccomp(seccomp_profile)
    audit.adjust_seccomp(container, rule_list, record_dir)
