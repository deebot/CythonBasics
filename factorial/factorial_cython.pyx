# cython: linetrace=True
# cython: profile=True
# distutils: define_macros=CYTHON_TRACE_NOGIL=1

cpdef float fact(int n):
    cpdef float product = 1
    while n > 0:
        product *= n
        n -= 1
    return product


def this_function_makes_line_profiler_to_print_all_the_way_down_here():
    pass


# Original pure python code

#def fact(n):
#    product = 1
#    while n > 0:
#        product *= n
#        n -= 1
#    return product


# Use Escape + 3 for commenting
