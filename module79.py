#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     04-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 84
#TIME MODULE

import time
print(4)
time.sleep(3)
print("this is printed after 3 seconds")

t=time.localtime()
formatted_time=time.strftime("%Y-%M-%D %H:%M:%S",t)
print(formatted_time)