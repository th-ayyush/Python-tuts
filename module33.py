#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     21-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 37
#finally keyword
'''finally keyword- code in it will get executed at all cost,if error was raised
ornot'''
def func1():
 try:
    l=[1,5,6,7]
    i=int(input("enter the index:"))
    print(l[i])
    return 1
 except:
    print("some error occured")
    return 0

 finally:
    print("im always executed")

 x=func1()
 print(x)