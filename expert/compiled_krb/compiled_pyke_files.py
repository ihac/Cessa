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
         ('', '', 'questions.kqb'):
           [1495374151.84925, 'questions.qbc'],
         ('', '', 'argument.kfb'):
           [1495374151.866534, 'argument.fbc'],
         ('', '', 'bc_relate.krb'):
           [1495374151.907056, 'bc_relate_bc.py'],
         ('', '', 'question_fact.kfb'):
           [1495374151.911798, 'question_fact.fbc'],
         ('', '', 'question_rule.krb'):
           [1495374151.915854, 'question_rule_bc.py'],
         ('', '', 'macro.kfb'):
           [1495374151.923852, 'macro.fbc'],
         ('', '', 'syscall.kfb'):
           [1495374151.97082, 'syscall.fbc'],
        },
        compiler_version)

