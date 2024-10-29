#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     22-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 44
#how import works in python

import math
result=math.sqrt(9)
print(result)
print(dir(math))#to know what functions contained by math library
print(math.nan,type(math.nan))#to know the what type of function is..

#if we want import particular function from a library

#from math import sqrt,pi

#result=pi(3)*sqrt(5)
#print(result)

#if we want to give particular name to a function
#from math import pi,sqrt as s

#result=s(9)*pi
#print(result)