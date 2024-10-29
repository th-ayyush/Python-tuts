#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     01-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#DAY 66
#INSTANCE VARIABLES VS CLASS VARIABLE

class employee:
    company="apple"
    def __init__(self,name):
        self.name=name
        self.raise_=0.02
    def showdetails(self):
            print(f"the name of the employee is {self.name} is {self.raise_}{self.company}")

emp1=employee("ayush")
emp1.raise_=0.03
emp1.company="apple india"#instance variable
emp1.showdetails()#if we will run this  it makesan error because it is passing one
#argument (emp1),but as shown it has no argument in showdetails()
employee.showdetails(emp1)#it will run

emp2=employee("rohan")
emp2.raise_=0.02
emp2.company="nestle"#instance variable
emp2.showdetails()

'''NOTE- "company" variable is a class variable,so it is applied in all over
the class. "name","raise " is an instance variable which means there will be
different variables for ayush,rohan and so on employees.

but "company" which is a class variable will applied for all the variables
IN emp1 we have given an instance variable "emp1.company=apple india",if there
is a instance variable for any object then it will be applies if not it will
look for class varaible'''