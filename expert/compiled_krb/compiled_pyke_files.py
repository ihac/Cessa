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
           [1495630581.250526, 'bc_relate_bc.py'],
         ('', '', 'macro.kfb'):
           [1495630581.269349, 'macro.fbc'],
         ('', '', 'argument.kfb'):
           [1495630581.270966, 'argument.fbc'],
         ('', '', 'questions.kqb'):
           [1495630581.277307, 'questions.qbc'],
         ('', '', 'syscall.kfb'):
           [1495630581.328257, 'syscall.fbc'],
         ('', '', 'question_fact.kfb'):
           [1495630581.329364, 'question_fact.fbc'],
         ('', '', 'question_rule.krb'):
           [1495630581.333748, 'question_rule_bc.py'],
        },
        compiler_version)

