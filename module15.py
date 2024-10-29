#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      User
#
# Created:     17-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day19
#break and continue

for i in range(12):

    if(i==10):
        break
    print("5 x",i+1,"=",5*(i+1))
print("exit loop")


for i in range(12):

    if(i==10):
        continue
    print("5 x",i+1,"=",5*i)
print("exit loop")