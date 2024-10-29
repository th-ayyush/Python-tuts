#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     18-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 24
#tuples
#they are unchangeable

tup=(1,5,6,7,"green")
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])


if"green" in tup:
    print("fuck you")

tup2=tup[1:4]
print(tup2)