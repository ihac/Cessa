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
           [1494137768.920293, 'bc_relate_bc.py'],
         ('', '', 'argument.kfb'):
           [1494137768.92855, 'argument.fbc'],
         ('', '', 'syscall.kfb'):
           [1494137768.930164, 'syscall.fbc'],
         ('', '', 'macro.kfb'):
           [1494137768.934469, 'macro.fbc'],
        },
        compiler_version)

