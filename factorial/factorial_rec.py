def fact( n ):
   if n <1:   # base case
       return 1
   else:
       returnNumber = n * fact( n - 1 )  # recursive call
       return returnNumber
