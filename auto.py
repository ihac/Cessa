#!/usr/bin/env python3
# encoding: utf-8

import json
from cessa.docker import ls_images, ls_containers
from cessa import trace, rule, profile, audit
from cessa.config import Action , Arch, Operator, Level
#workload = 'scripts/nginx-test.workload'
#trace_file = 'tmp/nginx.trace.list'
#REC_DIR = 'tmp'
#seccomp_profile = 'nginx-test.profile'

def auto_test():
    syscall_list = trace.data_preprocessing('tmp/nginx.trace.list', 'tmp')
    rule_coll_list = rule.gen_rules(syscall_list, REC_DIR='tmp', level=Level.ARG)
    seccomp = profile.Seccomp(Action.ERRNO)
    seccomp.set_arch([Arch.X86_64])
    seccomp.add_rules(rule_coll_list)
    json_profile = seccomp.to_json()
    return json.dumps(json_profile, indent=4, sort_keys=True)

def trace_test(container_name, image_id, opts=[]):
    trace_file = 'tmp/{}.trace'.format(container_name)
    record_dir = 'tmp/{}'.format(container_name)
    workload = 'scripts/{}.workload'.format(container_name)
    container = trace.Container(container_name, image_id)
    container.set_option(opts)
    container.set_workload(workload)
    trace.trace_syscall(container, trace_file)
    return container, trace.data_preprocessing(trace_file, record_dir)

def gen_rules_test(container, syscall_list, level=Level.NAME):
    record_dir = 'tmp/{}'.format(container.name)
    clabel_file = 'configs/{}.clabel.json'.format(container.name)
    rule_coll_list = rule.gen_rules(syscall_list, record_dir=record_dir, clabel_file=clabel_file, level=level)
    container.set_rules(rule_coll_list)

def dump_rules_test(container):
    seccomp_profile = 'profiles/{}.profile'.format(container.name)
    profile.dump_rules(seccomp_profile, container.rules)
    container.set_seccomp(seccomp_profile)

def adjust_test(container):
    audit.adjust_seccomp(container)

def all_test(container_name, image_id, opts=[], level=Level.NAME):
    container, syscall_list = trace_test(container_name, image_id, opts=opts)
    gen_rules_test(container, syscall_list, level=level)
    dump_rules_test(container)
    adjust_test(container)
