#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     30-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 61
#INHERITANCE

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"the name of employee: {self.id} is {self.name}")

class programmer(employee):
    def language(self):
        print("the default language is python")
e=employee("rohan",897)
e.showdetails()
e=programmer("hemy",890)
e.language()