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
         ('', '', 'argument.kfb'):
           [1494934798.955344, 'argument.fbc'],
         ('', '', 'bc_relate.krb'):
           [1494934798.983693, 'bc_relate_bc.py'],
         ('', '', 'macro.kfb'):
           [1494934798.990313, 'macro.fbc'],
         ('', '', 'syscall.kfb'):
           [1494934798.997499, 'syscall.fbc'],
        },
        compiler_version)

