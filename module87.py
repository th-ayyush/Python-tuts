#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     11-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 97
#MULTITHREADING -
''' suppose we have to downoad 10 files from internet and they are all from
different locations, if we download it one by on it wastes our time ,so
we can download them paarllel by using multithreading module'''

import threading
import time
#indicates some task being done
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)


time1=time.perf_counter()
#Normal code
#func(4)
#func(2)
#func(1)

#if we want to execute functions concurrently
#then we can target them as thread

#code using thread
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

t1.start()
t2.start()
t3.start()

time2=time.perf_counter()
print(time2-time1)


#NOTE- learn about threadpull executor