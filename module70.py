#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      User
#
# Created:     02-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 75
#EXERCISE 7 SOLUTION -CLEAR CLUTTER

import os
files=os.listdir("clutteredfolder")
i=1
for file in files:
    if file.endswith(".png"):
     print(file)
     os.rename("clutteredfolder/{file}",f"clutteredfolder/{i}.png")
     i=i+1