#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     17-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day15
#exercise2-good morning sir

time=int(input("enter the time according to 00-23 cycle:"))
if(time>=0 and time<12):
    print("Good morning sir")
elif(time>=12 and time<17):
    print("good afternoon sir")
elif(time>17 and time<21):
    print("good evening sir")
else:
    print("good night sir")

print("Have a good day sir")