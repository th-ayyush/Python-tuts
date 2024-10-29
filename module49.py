#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     26-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 53
#map,filter and reduce

#map
def cube(x):
    return x*x*x

l=[1,2,3,4,5]
newl=list(map(cube,l))
print(newl)
-
#filter
def filter_function(a):
    return a>4
newnewl=list(filter(filter_function,l))
print(newnewl)

#reduce
from functools import reduce
numbers=[1,2,3,4,5]
def mysum(x,y):
    return x+y

sum=reduce(mysum,numbers)
print(sum)