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
           [1494039260.118537, 'bc_relate_bc.py'],
         ('', '', 'argument.kfb'):
           [1494039260.128444, 'argument.fbc'],
         ('', '', 'syscall.kfb'):
           [1494039260.129771, 'syscall.fbc'],
        },
        compiler_version)

