#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     21-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#day 38
#custom errors
#raise keyword

a=int(input("enter the value between 5 and 9"))

if(a<5 or a>9):
    raise ValueError("VALUE SHOULD BE BETWEEN 5 AND 9")

#there are many in-built errors like value error in python...we can use them also


a=str(input("enter Keyword"))

if(a=="QUIZ"):
    print("succesful")
else:
    raise ValueError("VALUE SHOULD BE QUIZ")