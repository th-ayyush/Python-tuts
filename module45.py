#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     24-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 49
#file handling in python
#there are bulit-in nmethods of file handling in python

f=open('chemistry RG','rb')
#first attribute is file name and second attribute is mode of file
#'r' for read and 'w' for write and 'a' for append
text=f.read()
print(text)
f.close()

#there are various methods in python
#if we write using 'w'mode then ol content will be deleted
#if we want to add new things and want maintain th old data then we use 'a'

#WRITING A FILE
f.write('hello,world!')
f.open('myfile.txt','a')
f.close()

with open ('myfile.txt','a') as
 f:
  f.write('i am inside with')