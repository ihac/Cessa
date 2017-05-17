#!/usr/bin/env python3
# encoding: utf-8

import json
from cessa import trace, rule, profile, audit
from cessa.config import Action , Arch, Operator, Level
workload = 'scripts/nginx-test.workload'
trace_file = 'tmp/nginx.trace.list'
REC_DIR = 'tmp'
seccomp_profile = 'nginx-test.profile'

def auto_test():
    syscall_list = trace.data_preprocessing('tmp/nginx.trace.list', 'tmp')
    rule_coll_list = rule.gen_rules(syscall_list, REC_DIR='tmp', level=Level.ARG)
    seccomp = profile.Seccomp(Action.ERRNO)
    seccomp.set_arch([Arch.X86_64])
    seccomp.add_rules(rule_coll_list)
    json_profile = seccomp.to_json()
    return json.dumps(json_profile, indent=4, sort_keys=True)

def trace_test():
    container = trace.Container('nginx-test', '1e4e93130f1f')
    container.set_option(['-p', '8080:80'])
    container.set_workload(workload)
    trace.trace_syscall(container, trace_file)
    return container, trace.data_preprocessing(trace_file, REC_DIR)

def gen_rules_test(syscall_list, level=Level.NAME):
    rule_coll_list = rule.gen_rules(syscall_list, record_dir=REC_DIR, level=level)
    return rule_coll_list

def dump_rules_test(rule_coll_list):
    profile.dump_rules(seccomp_profile, rule_coll_list)

def adjust_test(container, rule_list):
    container.set_seccomp(seccomp_profile)
    audit.adjust_seccomp(container)
