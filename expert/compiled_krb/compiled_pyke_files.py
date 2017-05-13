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
         ('', '', 'syscall.kfb'):
           [1494663560.775203, 'syscall.fbc'],
         ('', '', 'macro.kfb'):
           [1494663560.779487, 'macro.fbc'],
         ('', '', 'argument.kfb'):
           [1494663560.781009, 'argument.fbc'],
         ('', '', 'bc_relate.krb'):
           [1494663560.803666, 'bc_relate_bc.py'],
        },
        compiler_version)

