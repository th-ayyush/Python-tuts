#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      User
#
# Created:     22-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 45

#what is "if__name__="__main__"
import ayush
harry.welcome()

def welcome():
    print("hey,you are welcome")

print(__name__)
if__name__=="__main__":
    ''' if we import a file from another module, without using
    if__name__=="__main__":  then we will get two same output because the file
    gets executed one time at its own place and second time at the place it is
    imported'''
    '''so to handle this situation we use if__name__=="__main__": so that the
    file gets executed at the place where it is imported ,not its own place'''
    welcome()