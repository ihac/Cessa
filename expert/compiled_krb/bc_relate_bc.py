# bc_relate_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def get_all_value(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('syscall', 'all_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_relate.get_all_value: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def get_type(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('syscall', 'arg_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_relate.get_type: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def get_index(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('syscall', 'arg_index', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_relate.get_index: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def get_macro_value(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('macro', 'define', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_relate.get_macro_value: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def strict_mode_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        value_list = []
        with engine.prove('argument', 'relevant', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_2:
          for x_2 in gen_2:
            assert x_2 is None, \
              "bc_relate.strict_mode_1: got unexpected plan from when clause 2"
            with engine.prove('syscall', 'all_value', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "bc_relate.strict_mode_1: got unexpected plan from when clause 3"
                for python_ans in \
                     context.lookup_data('value_relevant_tuple'):
                  mark4 = context.mark(True)
                  if rule.pattern(4).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    for python_ans in \
                         context.lookup_data('value_total_tuple'):
                      mark5 = context.mark(True)
                      if rule.pattern(4).match_data(context, context, python_ans):
                        context.end_save_all_undo()
                        value_list.append(context.lookup_data('value'))
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark5)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                mark7 = context.mark(True)
                if rule.pattern(5).match_data(context, context,
                        tuple(value_list)):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark7)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def strict_mode_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('argument', 'relevant', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_relate.strict_mode_2: got unexpected plan from when clause 1"
            with engine.prove('syscall', 'all_value', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_relate.strict_mode_2: got unexpected plan from when clause 2"
                for python_ans in \
                     context.lookup_data('value_relevant_tuple'):
                  mark3 = context.mark(True)
                  if rule.pattern(4).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    for python_ans in \
                         context.lookup_data('value_total_tuple'):
                      mark4 = context.mark(True)
                      if rule.pattern(4).match_data(context, context, python_ans):
                        context.end_save_all_undo()
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark4)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def loose_mode_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('syscall', 'all_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_relate.loose_mode_1: got unexpected plan from when clause 1"
            value_set = set(context.lookup_data('value_total_tuple'))
            with engine.prove('argument', 'conflicting', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "bc_relate.loose_mode_1: got unexpected plan from when clause 3"
                for python_ans in \
                     context.lookup_data('value_conflicting_value'):
                  mark4 = context.mark(True)
                  if rule.pattern(4).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    value_set.remove(context.lookup_data('value'))
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                mark6 = context.mark(True)
                if rule.pattern(5).match_data(context, context,
                        tuple(value_set)):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark6)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def loose_mode_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('syscall', 'all_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_relate.loose_mode_2: got unexpected plan from when clause 1"
            with engine.prove('argument', 'conflicting', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_relate.loose_mode_2: got unexpected plan from when clause 2"
                for python_ans in \
                     context.lookup_data('value_total_tuple'):
                  mark3 = context.mark(True)
                  if rule.pattern(4).match_data(context, context, python_ans):
                    context.end_save_all_undo()
                    if context.lookup_data('value') not in context.lookup_data('value_conflicting_value'):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark3)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_relate')
  
  bc_rule.bc_rule('get_all_value', This_rule_base, 'all_value',
                  get_all_value, None,
                  (contexts.variable('argument'),
                   contexts.variable('value_tuple'),),
                  (),
                  (contexts.variable('argument'),
                   contexts.variable('value_tuple'),))
  
  bc_rule.bc_rule('get_type', This_rule_base, 'arg_type',
                  get_type, None,
                  (contexts.variable('argument'),
                   contexts.variable('type'),),
                  (),
                  (contexts.variable('argument'),
                   contexts.variable('type'),))
  
  bc_rule.bc_rule('get_index', This_rule_base, 'arg_index',
                  get_index, None,
                  (contexts.variable('argument'),
                   contexts.variable('index'),),
                  (),
                  (contexts.variable('argument'),
                   contexts.variable('index'),))
  
  bc_rule.bc_rule('get_macro_value', This_rule_base, 'macro_value',
                  get_macro_value, None,
                  (contexts.variable('macro'),
                   contexts.variable('value'),),
                  (),
                  (contexts.variable('macro'),
                   contexts.variable('value'),))
  
  bc_rule.bc_rule('strict_mode_1', This_rule_base, 'accurate_value_tuple',
                  strict_mode_1, None,
                  (contexts.variable('argument'),
                   contexts.variable('label'),
                   contexts.variable('value_tuple'),),
                  (),
                  (contexts.variable('label'),
                   contexts.variable('value_relevant_tuple'),
                   contexts.variable('argument'),
                   contexts.variable('value_total_tuple'),
                   contexts.variable('value'),
                   contexts.variable('value_tuple'),))
  
  bc_rule.bc_rule('strict_mode_2', This_rule_base, 'accurate_value',
                  strict_mode_2, None,
                  (contexts.variable('argument'),
                   contexts.variable('label'),
                   contexts.variable('value'),),
                  (),
                  (contexts.variable('label'),
                   contexts.variable('value_relevant_tuple'),
                   contexts.variable('argument'),
                   contexts.variable('value_total_tuple'),
                   contexts.variable('value'),))
  
  bc_rule.bc_rule('loose_mode_1', This_rule_base, 'possible_value_tuple',
                  loose_mode_1, None,
                  (contexts.variable('argument'),
                   contexts.variable('label'),
                   contexts.variable('value_tuple'),),
                  (),
                  (contexts.variable('argument'),
                   contexts.variable('value_total_tuple'),
                   contexts.variable('label'),
                   contexts.variable('value_conflicting_value'),
                   contexts.variable('value'),
                   contexts.variable('value_tuple'),))
  
  bc_rule.bc_rule('loose_mode_2', This_rule_base, 'possible_value',
                  loose_mode_2, None,
                  (contexts.variable('argument'),
                   contexts.variable('label'),
                   contexts.variable('value'),),
                  (),
                  (contexts.variable('argument'),
                   contexts.variable('value_total_tuple'),
                   contexts.variable('label'),
                   contexts.variable('value_conflicting_value'),
                   contexts.variable('value'),))


Krb_filename = '../bc_relate.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 26), (4, 4)),
    ((39, 43), (7, 7)),
    ((45, 51), (9, 9)),
    ((64, 68), (12, 12)),
    ((70, 76), (14, 14)),
    ((89, 93), (17, 17)),
    ((95, 101), (19, 19)),
    ((114, 118), (22, 22)),
    ((120, 120), (24, 24)),
    ((121, 127), (25, 25)),
    ((128, 134), (26, 26)),
    ((136, 136), (28, 28)),
    ((141, 141), (29, 29)),
    ((145, 145), (30, 30)),
    ((152, 152), (31, 31)),
    ((168, 172), (34, 34)),
    ((174, 180), (36, 36)),
    ((181, 187), (37, 37)),
    ((189, 189), (38, 38)),
    ((194, 194), (39, 39)),
    ((214, 218), (42, 42)),
    ((220, 226), (44, 44)),
    ((227, 227), (45, 45)),
    ((228, 234), (46, 46)),
    ((236, 236), (48, 48)),
    ((240, 240), (49, 49)),
    ((245, 245), (50, 50)),
    ((261, 265), (53, 53)),
    ((267, 273), (55, 55)),
    ((274, 280), (56, 56)),
    ((282, 282), (57, 57)),
    ((286, 286), (58, 58)),
)
