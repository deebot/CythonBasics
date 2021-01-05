import time
import numpy

total = 0
num1 = 1000000000
arr = numpy.arange(num1, dtype=numpy.int64)

t1 = time.time()

for k in arr:
    total = total + k
print("Total = ", total)

t2 = time.time()
t = t2 - t1
print("%.20f" % t)
