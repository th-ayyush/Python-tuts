#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     09-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 93
#exercise 10 solution

 #USE NEWS API AND REQUEST MODULE

#day 94
#exercise 11 drink water reminder
import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(3600)
    return n*3600

print(fx(20))
print("Ae vedya,jaake paani pee warna bat ka grip nikaalkr")


#day 95
#regular expressions
import re
# with the help of re package we can find out the pattern in a large text
pattern="was"
text="i was suffering from depression, i was certainly not feeling well "
match=re.search(pattern,text)
print(match)
#it returns whether the pattern is in the text and where
#pattern=r"[A-Z]+yclone"
#[] defines capitalism
#there are many methods for searching the pattern
