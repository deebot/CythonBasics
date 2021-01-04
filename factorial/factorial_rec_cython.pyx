# cython: linetrace=True
# distutils: define_macros=CYTHON_TRACE_NOGIL=1

cpdef float fact(int n):
   cdef float returnNumber
   if n <1:   # base case
       return 1
   else:
       returnNumber = n * fact(n - 1)  # recursive call
       return returnNumber


def this_function_makes_line_profiler_to_print_all_the_way_down_here():
    pass


# Original pure python code

#def fact(n):
#   if n <1:   # base case
#       return 1
#   else:
#       returnNumber = n * fact(n - 1)  # recursive call
#       return returnNumber

