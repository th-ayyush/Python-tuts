#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     26-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 51
#some other file handling methods

'''if want to update some character in a file, rather than self-checking the
whole file we can use seek() method to search that character'''

#assume you have file names 'gye.txt' and have content that ayush is a good boy

with open ('gye.txt','r') as f:
    print(type(f))
    #move to the 10th byte in the file
    f.seek(10)

    #read the next 5 bytes
    data=f.read(5)
    print(data)

#tell() function

print(f.tell())#it tells that to much extent the seek() function is used
#like in above case seek() is used till 10 bytes

#truncate() method
#if we want to limit our file to certain characters then we use truncate

with open('sample.txt','w') as f:
    f.write('hello world')
    f.truncate(5)#if we runs this,then only hello will print

with open('sample.txt','r') as f:
    print(f.read())