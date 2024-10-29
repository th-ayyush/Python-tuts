#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     02-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#DAY 72
#super keyword

class parentclass:
    def parent_method(self):
        print("this is the parent")

class childclass(parentclass):
    def child_method(Self):
        print("this is the child method")
        super().parent_method()#it is used to call a method from parent class

child_object=childclass()
child_object.child_method()

'''NOTE- if child class have same name method as parent class ,then the method
which is in child class will be called first and method in parent class will
be called later'''


class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer:
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
rohan=employee("rohan das","420")
ayush=programmer("ayush","7898","python")
print(rohan.name)

