#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     03-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 77
#OPEARTOR OVERLOADING

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __add__(self,x):
        return vector(self.i+x.i,self.j+x.j,self.k+x.k)
v=vector(3,5,6)
print(v)
v1=vector(2,6,7)
print(v1)

print(v+v1)
print(type(v+v1))
