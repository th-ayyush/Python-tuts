#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     06-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 86
#WALRUS OPERATOR ->  :=

a=True
#if we print a=false without walrus it will give error
print(a:=False)
#we can give an expression within print like a=2
print(b:=2)

numbers=[1,2,3,45]
while (n:= len(numbers))>0:
    print(numbers.pop())


#foods=list()
#while true:
#   food=input("what food do you like?:")
#   if food=="quit":
#       break
#    foods.append(food)

foods=list()
while(food:=input("what food do you like?:"))!="quit":
    foods.append(food)