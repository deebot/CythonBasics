cdef extern from "mt19937ar.h":
    void init_genrand(unsigned long s)
    unsigned long genrand_int32()


