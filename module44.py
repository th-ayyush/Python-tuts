#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     24-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 48
#local vs global variables

x=4#global variable

def my_function():
    #if we want to change global variable inside a function
    global x
    x=4
    y=5#local variable
    print(y)


my_function()
print(x)
print(y)
'''this will cause an error because y is a local variable and is not
accessible outside of the function'''