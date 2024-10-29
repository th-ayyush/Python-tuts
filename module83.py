#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     09-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 91
#generators- it stores the information how to make values on the go
'''it means that values haven't stored previously but components is stored that
can be used to make values'''

def mygenerator():
    for i in range(5):
        yield i
        ''' it returns value for generator and suspend execution of
        function until next value is requested'''

gen=mygenerator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#they are generating values on the go rather than storing the values already
#it is memory efficient because it will return the values until we request them
#rather than storing all the values

