# distutils: sources=["mt19937ar.c"]
cimport mt

def init_state(unsigned long s):
    mt.init_genrand(s)

def rand_int32():
    return mt.genrand_int32()
