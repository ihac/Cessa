#!/usr/bin/env python3
# encoding: utf-8

from cessa import rule, trace
from cessa.config import Action, Level

syscall_list = trace.data_preprocessing('tmp/nginx.trace.list', 'tmp')
rule_list = rule.gen_rules(syscall_list, record_dir='tmp', level=Level.ARG)
print(len(rule_list))
for r in rule_list:
    print(r)
