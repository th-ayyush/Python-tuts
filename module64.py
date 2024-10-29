#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     01-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 69
#CLASS METHODS

class employee:
    company="apple"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")

    @classmethod#it is used so that first argument "cls" passed as class
    #by default instance is passed down
    #classmethod is used to change the class variable
    def chagecompany(cls,newcompany):
        cls.company=newcompany


e1=employee()
e1.name="ayush"
e1.show()
e1.chagecompany("tesla")
e1.show()
print(employee.company)