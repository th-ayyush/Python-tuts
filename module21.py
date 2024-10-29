#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      User
#
# Created:     18-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-----------------------------------------------------------------

#day 25
# methods in tuples

#if you want to manipulate tuple then you have to fisrt coonvert it in the list
#then make changes and after  that convert it in tuple again

countries=("spain","india","italy","england")
temp=list(countries)#this converts tuple into list
temp.append("russia")
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)#again convert list in tuple
print(countries)


tuple1=(0,1,2,3,4,5,5,4,3,2,1)
res=tuple1.count(3)#counts occurence of 3
print(res)

tuple1=(0,1,2,3,4,5,5,4,3,2,1)
res=tuple1.index(5)#returns index
print(res)
