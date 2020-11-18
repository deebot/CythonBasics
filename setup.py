# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:55:51 2020

@author: Armin Weigold
"""

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("testcython.pyx")
)
print ("hello there")