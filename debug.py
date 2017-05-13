#!/usr/bin/env python3
# encoding: utf-8

from cessa import rule, trace
from cessa.config import Action, Level

syscall_list = trace.data_preprocessing('tmp/nginx.trace.list', 'tmp')
rule_coll_list = rule.gen_rules(syscall_list, record_dir='tmp', level=Level.ARG)
print(len(rule_coll_list))
for r_c in rule_coll_list:
    print(r_c.name, r_c.level)
    for r in r_c.rules:
        print('\t', r)
