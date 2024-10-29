#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     19-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 29
#docstrings

#it is used to describe the functions,class etc.


def square(n):
   '''takes in a number n,returns the square of n'''#docstring
   #it is written just after the function definition
   print(n**2)


square(5)
print(square.__doc__)#__doc__ is used to print the docstring of a fuction,class.