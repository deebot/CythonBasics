
#setup.py file

from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Compiler.Options import get_directive_defaults
directive_defaults = get_directive_defaults()

directive_defaults['linetrace'] = True
directive_defaults['binding'] = True

extensions = [Extension("*", ["*.pyx"],define_macros=[('CYTHON_TRACE', '1')])]

setup(ext_modules =cythonize(extensions,annotate= True))
