#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     11-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 98
#multiprocessing

import multiprocessing
#import requests

def downloadfile(url,name):
    response=requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)


url="https://picsum.photos/200/300"
for _ in range(5):
    downloadfile(url,i)

#NOTE-do it on repel or vs code

#day 99
#exercise 11 solution

import os
command= *osascript -e \'say \*hey,ayush drink water\*\';osascript -e \'display alert\*hey aysuh,drink water\*\'*
os.system(command)