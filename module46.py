#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     26-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 5o
#read(),readlines() and other methods of file handling


#if you want to read many lines at same time
f=open('gy.xt','r')
i=0
while True:
    i=i+1
    line=f.readlines()#read until there is line in file
    if not line:
        break
    #if we reading different marks from another file like
    #34,56,47
    #22,34,89
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    print("marks of students {i} in maths is:{m1}")
    print("marks of students {i} in english is:{m2}")

    print(line,type(line))


#writelines method
f=open('myfile.txt','w')
lines=['line 1\n','line2\n','line3\n']
f.writelines(lines)
f.close()
