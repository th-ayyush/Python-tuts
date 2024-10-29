#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     18-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 23
#list methods

l=[1,2,5,6]
print(l)
print(l.append(7))#it adds element in list at last

print(l.sort())#it makes list in ascending order
print(l.sort(reverse=True))#it makes list in descending order
print(l.reverse())
print(l.index(1))#it returns index of 1
print(l.count(2))#it counts no. of occurence

m=l.copy()#it copies the list in another variable
print(m)

l.insert(1,899)#it inserts 899 at index1
print(l)

n=[656,66,10]
l.extend(n)#it means take all elements of m and add it at last of list l
print(l)

o=n+l#it concatenates n and l in o