#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     28-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 58
#constructors

class person:
    def __init__(self,name,occ):
        print("hey i am ayush")
        self.name=name
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("ayush","hr")
b=person("gaurav","manager")
a.info()
b.info()