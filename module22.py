#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     19-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#exercise 2 solution by time module
import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
#=int(input("enter hour:"))
#print(hour)

if(hour>=0 and hour<12):
    print("good morning,sir")
elif (hour>12 and hour<17):
    print("good afternoon,sir")
elif(hour>=17 and hour<0):
    print("good night,sir")