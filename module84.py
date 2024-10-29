#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     09-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 92
#function caching

import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
#it have a time gap of 5
#if we copy the print section again
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
'''and run it after the first print section,second will not take 5sec to get
executed because it knows what value of 20,2,6 wiil be,it takes values from
the cache generated earlier by the first print section,so thats it will get
executed immediately after the first section'''