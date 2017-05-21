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
           [1495335069.16785, 'macro.fbc'],
         ('', '', 'syscall.kfb'):
           [1495335069.183489, 'syscall.fbc'],
         ('', '', 'question_rule.krb'):
           [1495335069.190801, 'question_rule_bc.py'],
         ('', '', 'argument.kfb'):
           [1495335069.19258, 'argument.fbc'],
         ('', '', 'questions.kqb'):
           [1495335069.204699, 'questions.qbc'],
         ('', '', 'question_fact.kfb'):
           [1495335069.20759, 'question_fact.fbc'],
         ('', '', 'bc_relate.krb'):
           [1495335069.246141, 'bc_relate_bc.py'],
        },
        compiler_version)

