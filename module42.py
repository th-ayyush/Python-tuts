#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     24-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#day 46
#os module-built-in module

import os

if(not os.path.exists("data")):
  os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day(i+1)")


for i in range(0,100):
    os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")

#when you have to perform actions on bulk of files ,you can use os mudule


folders=os.listdir("data")
print(folders)#it prints all the folders contained in the

for folder in folders:
    print(folder)