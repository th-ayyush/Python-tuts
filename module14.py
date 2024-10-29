#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      User
#
# Created:     17-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 18
#while loops

i=0
while(i<3):
    print(i)
    i=i+1

print("done with the loop")


i=int(input("enter no."))
while(i<3):
    i=int(input("enter the no."))
    print(i)
print("done with the loop")

#decrementing loop
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("i\'m inside a loop")