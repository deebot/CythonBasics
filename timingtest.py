# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:34:59 2020

@author: Armin Weigold
"""

import timeit

cy=timeit.timeit('testcython.variables()',setup='import testcython',number=10000)
py=timeit.timeit('purepython.variables()',setup='import purepython',number=10000)
print(cy,py)
print('Cython is {}Xtimes faster'.format(py/cy))
