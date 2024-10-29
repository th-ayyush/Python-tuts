#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      User
#
# Created:     20-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day35
#for loop with else

for i in []:
    print(i)
#if control cannot ne passed in for loop then else will be executed

else:
    print("sorry no i")


i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break#if we don't use break else will also be executed

else:
    print ("sorry no i")
    '''if loop is sucessful then else will be executed,not
    breaking the loop'''