#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     20-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#methods in sets


s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)#it means all values of s2 get store in s1
s1.intersection(s2)
s3=s2.symmetric_difference(s1)#a-b in set

print(s1,s2)

#disjoint set-both set have diffrent elements
d={1,2,3}
e={4,5,6}
print(d.isdisjoint(e))

#superset- is b elements is present in a
d={1,2,3,4,5,6}
e={4,5,6}
print(e.issuperset(d))


#subset
d={1,2,3}
e={1,2}
print(e.issubset(d))

#add
d={1,2,3}
d.add(87)#to add one item
d.remove(1)#if item is not present then error will be raised
d.discard(2)#if item is not present then error will not be raised
#clear is used to clear the complete list
#pop is used to delete the random value from the list
print(d)