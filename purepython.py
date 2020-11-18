# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:35:40 2020

@author: Armin Weigold
"""
from random import *



def variables():
    
    
    
    list = [0,1,2,3,4,5,6,7,8,9]
    i = 0
    while i < 20:
        x = randint(0 , 9)
        count = 0
        snumber = 0
        rnumber = x
        for j in list:
            
           
            
            
            snumber =list[count ]  
            list[count ] = rnumber 
            rnumber = snumber
            
            count = count +1
        print (list)
        i = i + 1
    
