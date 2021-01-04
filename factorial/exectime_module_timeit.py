import timeit
my_mod1 ="import factorial_cython"
my_mod2 = "import factorial"
cy_exec = timeit.timeit(setup = my_mod1, stmt = 'factorial_cython.fact(994)',number = 100000)

py_exec = timeit.timeit(setup = my_mod2,stmt = 'factorial.fact(994)', number = 100000)

print("Cython code execution time: %s seconds" %cy_exec)
print("Python code execution time: %s seconds" %py_exec)
print("Cython_execution is %s times faster as Python's"%(py_exec/cy_exec))

