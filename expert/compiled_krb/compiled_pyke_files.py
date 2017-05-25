# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'macro.kfb'):
           [1495724995.415348, 'macro.fbc'],
         ('', '', 'syscall.kfb'):
           [1495724995.456122, 'syscall.fbc'],
         ('', '', 'argument.kfb'):
           [1495724995.458212, 'argument.fbc'],
         ('', '', 'bc_relate.krb'):
           [1495724995.500693, 'bc_relate_bc.py'],
         ('', '', 'question_fact.kfb'):
           [1495724995.501994, 'question_fact.fbc'],
         ('', '', 'questions.kqb'):
           [1495724995.511563, 'questions.qbc'],
         ('', '', 'question_rule.krb'):
           [1495724995.518342, 'question_rule_bc.py'],
        },
        compiler_version)

