import timeit

cy=timeit.timeit('prime_cython.primes(10)',setup='import prime_cython',number=10000)
py=timeit.timeit('prime_pure.primes(10)',setup='import prime_pure',number=10000)
print(cy,py)
print('Cython is {}Xtimes faster'.format(py/cy))