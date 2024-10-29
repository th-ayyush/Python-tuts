#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     02-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 71
#dir, __dict__ and help method

x=[1,2,3]
print(dir(x))#by this we can know all methods about it
print(x.__add__)
#you can use this on tuple,list

#__dict__
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person("john",30)
print(p.__dict__)#it takes all attributes of class as dictionary
#whixh means name,age will considered in a dictionary

#help

print(help(person))#it tells you all about class