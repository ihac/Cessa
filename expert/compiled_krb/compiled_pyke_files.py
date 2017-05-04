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
           [1493905576.672846, 'argument.fbc'],
         ('', '', 'bc_relate.krb'):
           [1493905576.696236, 'bc_relate_bc.py'],
         ('', '', 'syscall.kfb'):
           [1493905576.697468, 'syscall.fbc'],
        },
        compiler_version)

