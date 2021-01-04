
#setup.py file

from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler.Options import get_directive_defaults
directive_defaults = get_directive_defaults()

directive_defaults['linetrace'] = True #enables profiling
directive_defaults['binding'] = True
directive_defaults ['language_level'] = 3 #enable python3 semantics
# distutils: define_macros=CYTHON_TRACE_NOGIL=1

extensions = [Extension("*", ["*.pyx"],define_macros=[('CYTHON_TRACE', '1')])]

setup(ext_modules =cythonize(extensions, compiler_directives = {'linetrace': True},annotate= True)) #linetrace compiler directive to enable both profiling and line tracing
