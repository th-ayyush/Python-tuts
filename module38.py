#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     22-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 42
#enumerate function

a=[23,12,45,89,34,67]

index=0
for index,mark in enumerate(a):
    print(mark)
    if(index==3):
        print("wow!")
    #index+=1
    #you don't have to write this