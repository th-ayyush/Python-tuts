#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     21-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 36
#exception handling

a=input('enter the number')
print(f"multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)}X {i}={int(a)*i}")
except:
    print("invalid syntax")
'''if we use try,then the only that has error will not execute,except that all
instructions will get executed'''
print("some imp. lines of code")
print("end of program")



