#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     28-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 56
#INTRO TO OOPS


#day 57
class person:
    name="ayush"
    occupation="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a=person()
b=person()
c=person()
a.name="gye"
a.occupation="hr"

b.name="vishal"
b.occupation="accountant"
#a.name="ajay"
#occupation="chutiya"
#print(a.name,a.occupation)

a.info()
b.info()
c.info()