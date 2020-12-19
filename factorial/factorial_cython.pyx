cpdef float fact(int n):
    cpdef float product = 1
    while n > 0:
        product *= n
        n -= 1
    return product


#def fact(n):
#    product = 1
#    while n > 0:
#        product *= n
#        n -= 1
#    return product


# Use Escape + 3 for commenting
