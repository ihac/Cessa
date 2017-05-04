# bc_relate_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def range1(rule, arg_patterns, arg_context):
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
              "bc_relate.range1: got unexpected plan from when clause 2"
            with engine.prove('argument', 'all_value', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "bc_relate.range1: got unexpected plan from when clause 3"
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

def range2(rule, arg_patterns, arg_context):
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
              "bc_relate.range2: got unexpected plan from when clause 1"
            with engine.prove('argument', 'all_value', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_relate.range2: got unexpected plan from when clause 2"
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

def range3(rule, arg_patterns, arg_context):
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
              "bc_relate.range3: got unexpected plan from when clause 1"
            if context.lookup_data('value') in context.lookup_data('value_relevant_tuple'):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def range4(rule, arg_patterns, arg_context):
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
              "bc_relate.range4: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_relate')
  
  bc_rule.bc_rule('range1', This_rule_base, 'accurate_values',
                  range1, None,
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
  
  bc_rule.bc_rule('range2', This_rule_base, 'accurate_value',
                  range2, None,
                  (contexts.variable('argument'),
                   contexts.variable('label'),
                   contexts.variable('value'),),
                  (),
                  (contexts.variable('label'),
                   contexts.variable('value_relevant_tuple'),
                   contexts.variable('argument'),
                   contexts.variable('value_total_tuple'),
                   contexts.variable('value'),))
  
  bc_rule.bc_rule('range3', This_rule_base, 'test',
                  range3, None,
                  (contexts.variable('argument'),
                   contexts.variable('label'),
                   contexts.variable('value'),),
                  (),
                  (contexts.variable('label'),
                   contexts.variable('value_relevant_tuple'),))
  
  bc_rule.bc_rule('range4', This_rule_base, 'test2',
                  range4, None,
                  (contexts.variable('label'),
                   contexts.variable('value'),),
                  (),
                  (contexts.variable('label'),
                   contexts.variable('value'),))


Krb_filename = '../bc_relate.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 20), (4, 4)),
    ((21, 27), (5, 5)),
    ((28, 34), (6, 6)),
    ((36, 36), (8, 8)),
    ((41, 41), (9, 9)),
    ((45, 45), (10, 10)),
    ((52, 52), (11, 11)),
    ((68, 72), (14, 14)),
    ((74, 80), (16, 16)),
    ((81, 87), (17, 17)),
    ((89, 89), (18, 18)),
    ((94, 94), (19, 19)),
    ((114, 118), (22, 22)),
    ((120, 126), (24, 24)),
    ((127, 127), (25, 25)),
    ((140, 144), (28, 28)),
    ((146, 152), (30, 30)),
)
