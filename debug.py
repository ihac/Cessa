#!/usr/bin/env python3
# encoding: utf-8

from cessa import rule, trace
from cessa.config import Action, Level
CLABEL_FILE='configs/clabel.json'
RECORD_DIR='tmp'

syscall_list = trace.data_preprocessing('tmp/nginx-test.trace', 'tmp')
# rule_coll_list = rule.gen_rules(syscall_list, level=Level.NAME)
#rule_coll_list = rule.gen_rules(syscall_list, record_dir='tmp', level=Level.ARG)
#rule_coll_list = rule.gen_rules(syscall_list, record_dir=RECORD_DIR, clabel_file=CLABEL_FILE, level=Level.CLABEL)
rule_coll_list = rule.gen_rules(syscall_list, record_dir=RECORD_DIR, clabel_file=CLABEL_FILE, level=Level.CUSTOM)
print(len(rule_coll_list))
#print(rule_coll_list)
for r_c in rule_coll_list:
    #print(r_c)
    print(r_c.name, r_c.level)
    for r in r_c.rules:
        print('\t', r)
