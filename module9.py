#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     16-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#string methods

a="!Ayush!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#it removes the trailing strips not the strips in starting
print(a.replace("Ayush","batman"))
print(a.split(" "))

#to make the first letter of string capital and all other uppercase in lower case
mango="hye,i am ayush"
print(mango.capitalize())


str1="welcome to gurgaon"
print(len(str1))
print(len(str1.center(50)))
print(str1.count("g"))#to count the appearances of a particular string

#to check a situation
str2="las vegas!!!"
print(str2.endswith("!!!"))
print(str2.find("a"))#return index of a particular character


#to check alphanumeric string
str3="royal rumble"