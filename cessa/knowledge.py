#!/usr/bin/env python3
# encoding: utf-8

from pyke import knowledge_engine
es_engine = knowledge_engine.engine((None, 'expert.compiled_krb'))
# es_engine = knowledge_engine.engine((None, 'cessa/compiled_knowledge'))

es_engine.activate('bc_relate')

# def get_possible_value(syscall, arg_idx):
    # """TODO: Docstring for get_possible_value.

    # :syscall: TODO
    # :arg_idx: TODO
    # :returns: TODO

    # """
    # pass

def get_value_range(arg_name):
    """ gets all possible value of argument if it has a value range.
    Users have to make sure the argument does have value range!

    :arg_name: argument name
    :returns: value tuple

    """
    try:
        macro_tuple = es_engine.prove_1_goal('bc_relate.all_value({}, $macro_tuple)'.format(arg_name))[0]['macro_tuple']
        return tuple(map(lambda x: get_value(x), macro_tuple))
    except:
        raise RuntimeError('Cannot prove goal in get_arg_type() with arg_name = \'{}\''.format(arg_name))

def get_arg_type(arg_name):
    """ gets argument type from knowledge engine

    :arg_name: argument name
    :returns: type string

    """
    try:
        with es_engine.prove_goal('bc_relate.arg_type({}, $type)'.format(arg_name)) as gen:
            for var, _ in gen:
                return var['type']
            return 'other'
    except:
        raise RuntimeError('Cannot prove goal in get_arg_type() with arg_name = \'{}\''.format(arg_name))

def get_value(c_macro):
    """ gets value of C macro

    :c_macro: macro in C. E.g, AF_INET
    :returns: value of C macro

    """
    # my_goal = goal.compile('bc_relate.get_value($macro)')
    try:
        with es_engine.prove_goal('bc_relate.macro_value({}, $value)'.format(c_macro)) as gen:
            for var, _ in gen:
                return var['value']
            return None
    except:
        raise RuntimeError('Cannot prove goal in get_value() with c_macro = \'{}\''.format(c_macro))

def get_index(arg_name):
    """ gets index of arg_name

        E.g, socket(domain, type, protocol)
        socket_domain's index = 0, socket_type's index = 1, ...

    :arg_name: argument name
    :returns: index

    """
    try:
        with es_engine.prove_goal('bc_relate.arg_index({}, $index)'.format(arg_name)) as gen:
            for var, _ in gen:
                return var['index']
            return None
    except:
        raise RuntimeError('Cannot prove goal in get_index() with arg_name = \'{}\''.format(arg_name))

def get_related_args(arg_name_list):
    """ get related set from the argument list if exists

    :arg_name_list: argument name list
    :returns: related set or None

    """
    return None
