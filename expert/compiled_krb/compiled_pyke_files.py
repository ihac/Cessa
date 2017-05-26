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
           [1495806479.467554, 'bc_relate_bc.py'],
         ('', '', 'macro.kfb'):
           [1495806479.482404, 'macro.fbc'],
         ('', '', 'question_rule.krb'):
           [1495806479.485409, 'question_rule_bc.py'],
         ('', '', 'argument.kfb'):
           [1495806479.487064, 'argument.fbc'],
         ('', '', 'questions.kqb'):
           [1495806479.495429, 'questions.qbc'],
         ('', '', 'syscall.kfb'):
           [1495806479.559821, 'syscall.fbc'],
         ('', '', 'question_fact.kfb'):
           [1495806479.561614, 'question_fact.fbc'],
        },
        compiler_version)

