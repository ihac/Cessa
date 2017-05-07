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
           [1494159139.616877, 'argument.fbc'],
         ('', '', 'syscall.kfb'):
           [1494159139.620173, 'syscall.fbc'],
         ('', '', 'macro.kfb'):
           [1494159139.62436, 'macro.fbc'],
         ('', '', 'bc_relate.krb'):
           [1494159139.65367, 'bc_relate_bc.py'],
        },
        compiler_version)

