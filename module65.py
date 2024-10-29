#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     02-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 70
#CLASS METHODS as ALTERNATIVE CONSTRUCTORS

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        #class method as alternativ constructors
    @classmethod
    def fromstr(cls,string):
            return cls(string.split("-")[0],string.split("-")[1])

e=employee("ayush",12000)
print(e.name)
print(e.salary)
#if information is given as string like "ayush-12000" and we have extract the data
#string="hurray-15000"
#e=employee(string.split("-"),12000)#by split it becomes list
#e1=employee(string.split("-")[0],string.split("-")[1])
#print(e1.name)
#print(e1.salary)

#BY USING CLASS METHOD
string="joker-30000"
e2=employee.fromstr(string)
print(e2.name)
print(e2.salary)