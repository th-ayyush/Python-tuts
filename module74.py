#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     03-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 79
#MULTIPLE INHERITANCE


class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
            print(f"the name is {self.name}")
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
            print(f"the dance is{self.dance}")

class danceremployee(employee,dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=dance
o=danceremployee("kathak","shivani")
print(o.name)
print(o.dance)
o.show()
print(danceremployee.mro())