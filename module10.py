#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     17-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day14
#if-else
#conditional operators
# >,<,>=,<=,==,!=
a=int(input("enter your age"))
print("your age is:",a)

if(a>18):
    print("you can drive")
else:
    print("you cannot derive")



appleprice=210
budget=200
if(appleprice<=budget):
    print("alexa,add 1kg to cart")
else:
    print("alexa,do  not add apples to the cart")



appleprice=10
budget=200
if(budget-appleprice>50):
    print("alexa,add 1kg to cart")
elif(budget-appleprice>70):
    print("its okay you can buy")
else:
    print("alexa,do  not add apples to the cart")



num=18
if(num<0):
    print("number is negative"):
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is between 11-20")
    else:
        print("number is greter than 20")
else:
    print("number is zero")