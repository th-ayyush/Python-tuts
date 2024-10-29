#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     18-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day22
#list

#contain different data types in a single block
#sign = [ ]
#it have ordered behaviour
#it can be altered


marks=[3,5,6,"ayush",True]
print(marks)
print(marks[2])
print(marks[-2])#negative indexing

if 7 in marks:
    print("yes")
else:
    print("no")


if "ay" in "ayush":
    print("hello")

print(marks[1:])#it will take len of marks after :
print(marks[:4])#it wiil take 0 before :
print(marks[1:-1])
print(marks[1:4:2])
#in this the value on 2nd index/jumped is skipped between index 1-4


#list comprehension

lst=[i*i for i in range(4)]
print(lst)


lst=[i*i for i in range(10) if i%2==0]
print(lst)
