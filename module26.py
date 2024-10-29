#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      User
#
# Created:     19-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#day 30
#recursion
#calling the same function in itself.


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
#5*factorial(4)
#5*4*factorial(3)
#5*4*3*factorial(2)
#5*4*3*2*factorial(1)
#in next step condition n==1 get true
#5*4*3*2*1


#quick quiz for fibonacci series

