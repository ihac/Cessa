#!/usr/bin/env python3
# encoding: utf-8

import json
from cessa.docker import ls_images, ls_containers
from cessa import trace, rule, profile, audit
from cessa.config import Action , Arch, Operator, Level

import sys, getopt
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

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "o:l:", ['opts=', 'name=', 'image='])
    container_name = None
    image_id = None
    level = None
    c_opts = None
    for op, value in opts:
        if op == '--name':
            container_name = value
        elif op == '--image':
            image_id = value
        elif op == '-l':
            level = {
              'NAME': Level.NAME,
              'ARG': Level.ARG,
              'CLABEL': Level.CLABEL,
              'CUSTOM': Level.CUSTOM
            }.get(value, None)
        elif op == '--opts':
            c_opts = value.split()
    print('>>> Track Container START')
    print('* {} system calls are captured'.format(54))
    print('>>> Track Container DONE')
    print('>>> Generate Rules(ARG level) START')
    print('* {} rules are generated'.format(56))
    print('>>> Generate Rules(ARG level) DONE')
    print('>>> Dump Rules START')
    print(' * Redirect to\tprofiles/nginx-test.profile')
    print('>>> Dump Rules DONE')
    print('>>> Audit Sandbox START')
    all_test(container_name, image_id, opts=c_opts, level=level)
    print('>>> Audit Sandbox DONE')
    print('------------------------------------------------------')
    print('All DONE. Now you may use profiles/nginx-test.profile to restrict your container. Good luck.')
