# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:58:40 2020

@author: Armin Weigold
"""
from random import *


def variables():

   
    
    cdef int L [10]
    cdef int i = 0
    cdef int count = 0
    cdef int snumber = 0
    cdef int rnumber = 0
    cdef int x 
    while i < 20:
        x = randint(0 , 9)
        count = 0
        snumber = 0
        rnumber = x
        
        for j in list:
            
            snumber =L[count ]  
            L[count ] = rnumber 
            rnumber = snumber
            
            count = count +1
        print (list)
        i = i + 1
        
    
