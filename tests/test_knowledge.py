#!/usr/bin/env python3
# encoding: utf-8

# import pytest

from cessa import knowledge

# def test_get_possible_value():
    # value_tuple = knowledge.get_possible_value()
    # assert

def test_get_value_range():
    value_range = knowledge.get_value_range('socket_domain')
    assert sorted(value_range) == [1, 2, 3, 4, 5, 8, 9, 10, 16, 17, 38]

def test_get_arg_type():
    arg_type = knowledge.get_arg_type('socket_domain')
    assert arg_type == 'range'
    arg_type = knowledge.get_arg_type('socket_type')
    assert arg_type == 'range'
    arg_type = knowledge.get_arg_type('socket_protocol')
    assert arg_type == 'other'

def test_get_value():
    value = knowledge.get_value('AF_INET')
    assert value == 2
    value = knowledge.get_value('SOCK_RAW')
    assert value == 3

def test_get_index():
    index = knowledge.get_index('socket_domain')
    assert index == 0
    index = knowledge.get_index('socket_protocol')
    assert index == 2
