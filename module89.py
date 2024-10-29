#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     11-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#Fibonacci series
a=0
b=1

print(a)
print(b)

for i in range(2,11):
    c=a+b
    a=b
    b=c
    print(c)

#Palindrome number

num= int(input("enter a number"))
temp=num
rev=0
while num >0:
    dig =  num%10
    rev=rev*10 + dig
    num =num // 10

if rev==temp:
    print("it is plaindrome")
else:
    print("it is not")

