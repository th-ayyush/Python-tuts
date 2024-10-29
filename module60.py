#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      User
#
# Created:     30-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 65
#static methods

class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b

a=Math(6)
print(a.num)
a.addtonum(7)
print(a.num)

print(a.add(7,2))
print(Math.add(8,9))

'''Note-To make a method in class we does need to pass self as an argument
everytime, we can use static method instead of it '''