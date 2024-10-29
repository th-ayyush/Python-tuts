#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     18-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day21
#functions with arguments

def average(a=9,b=1):#these are default values as arguments
    print("the average is",(a+b)/2)

#average(4,6)
average(4)#here we have taken a value=4 and b will be taken from default values


def name(fname,mname="john",lname="watson"):
    print("hello",fname,mname,lname)

name("amy","aggarwal","jain")

#variable length arguments

def average(*numbers):#numbers will be taken as tuple
    sum=0
    for i in numbers:
        sum=sum+i
    #print("average is:",sum/len(numbers))
    return sum/len(numbers)
c=average(5,6,7,1)
print(c)
