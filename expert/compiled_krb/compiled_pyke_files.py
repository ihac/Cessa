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
         ('', '', 'bc_relate.krb'):
           [1495107420.334188, 'bc_relate_bc.py'],
         ('', '', 'syscall.kfb'):
           [1495107420.342045, 'syscall.fbc'],
         ('', '', 'questions.kqb'):
           [1495107420.347755, 'questions.qbc'],
         ('', '', 'argument.kfb'):
           [1495107420.349176, 'argument.fbc'],
         ('', '', 'macro.kfb'):
           [1495107420.353362, 'macro.fbc'],
         ('', '', 'question_fact.kfb'):
           [1495107420.354085, 'question_fact.fbc'],
         ('', '', 'question_rule.krb'):
           [1495107420.356874, 'question_rule_bc.py'],
        },
        compiler_version)

