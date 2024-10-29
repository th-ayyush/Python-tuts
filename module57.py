#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     30-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#day 62
#ACCESS MODIFIERS
#Public,Protected,Private
'''NOTE-there is nothing like public,protected,private in python but we can use
it by some methods'''


#by default without mentioning everything in python is public
class employee:
    def __init__(self):
        self.name="ayush"

a=employee()
print(a.name)

#private
#when we use double underscore infront of any prefix, it becomes private
class kola:
    def __init__(self):
        self.__na="ayush"


#NOTE-In python there is no strictness for private modifier like other language
#To access private part
b=kola()
#print(b.__name) - cannot be access directly
print(b._kola__na)#can be access indirectly

#protected
#when we use single underscore infornt of a prefix it becomes protected
'''protected which cannot be accessed from outside of the class but can be
accessed by sub-classes or inherited classes'''


