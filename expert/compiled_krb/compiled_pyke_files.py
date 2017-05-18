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
           [1495099138.677598, 'bc_relate_bc.py'],
         ('', '', 'syscall.kfb'):
           [1495099138.687177, 'syscall.fbc'],
         ('', '', 'macro.kfb'):
           [1495099138.691546, 'macro.fbc'],
         ('', '', 'questions.kqb'):
           [1495099138.697755, 'questions.qbc'],
         ('', '', 'argument.kfb'):
           [1495099138.699238, 'argument.fbc'],
        },
        compiler_version)

