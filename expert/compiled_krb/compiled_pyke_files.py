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
           [1494676849.647883, 'bc_relate_bc.py'],
         ('', '', 'macro.kfb'):
           [1494676849.656128, 'macro.fbc'],
         ('', '', 'argument.kfb'):
           [1494676849.657713, 'argument.fbc'],
         ('', '', 'syscall.kfb'):
           [1494676849.66101, 'syscall.fbc'],
        },
        compiler_version)

