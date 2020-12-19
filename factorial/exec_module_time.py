import time
start_time = time.time()
import factorial_rec_cython
for i in range(100000):
  factorial_rec_cython.fact(994)

cy_exec = (time.time() - start_time)

time.sleep(3)

start_time = time.time()
import factorial_rec
for i in range(100000):
  factorial_rec.fact(994)

py_exec = (time.time() - start_time)
print("Cython code execution time: %s seconds" %cy_exec)
print("Python code execution time: %s seconds" %py_exec)
print("Cython_execution is %s times faster as Python's"%(py_exec/cy_exec))
