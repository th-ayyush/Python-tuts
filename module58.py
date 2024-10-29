#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     30-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 63
#exercise 5 solution


import random
def check(comp,user):
    if comp==user:
        return 0
    if(comp==0 and user ==1):
        return -1
    if(comp==1 and user ==2):
        return -1
    if(comp==2 and user ==0):
        return -1

    return 1
comp=random.randint(0,2)
user=int(input("o for snake,1 for water and -1 for gun"))

score=check(comp,user)
print("you:",user)
print("computer",comp)
if(score==0):
    print("its a draw")
elif(score==-1):
    print("you lose")
else:
    print("you won")