#!/usr/bin/env python3
# encoding: utf-8

from pyke import knowledge_engine

engine = knowledge_engine.engine(__file__)
engine.activate('bc_relate')

def foo():
    engine.prove_1_goal('bc_relate.test2(socket_domain, ipv4, $value)')
