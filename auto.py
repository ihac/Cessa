#!/usr/bin/env python3
# encoding: utf-8

import json
from cessa import trace, rule, profile
from cessa.config import Action , Arch

def auto_test():
    syscall_list = trace.data_preprocessing('tmp/nginx.trace.list', 'tmp')
    rules2 = rule.gen_rules(syscall_list, 'tmp', None, level='normal')
    seccomp = profile.Seccomp(Action.ERRNO)
    seccomp.set_arch([Arch.X86_64])
    seccomp.set_rules(rules2)
    json_profile = seccomp.to_json()
    return json.dumps(json_profile, indent=4, sort_keys=True)
