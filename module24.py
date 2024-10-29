#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     19-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 28
#f-strings= is is used for string formatting

letter="hey my name is {} and i am from {}"
country="india"
name="ayush"
#the values of country and name gets placed in the {}
print(letter.format(country,name))#it is older method


print(f"hey my name is {name} and i am from {country}")

price=49.999
txt = f"for only {price:.2f} dollars!"
print(txt)