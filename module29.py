#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     20-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 33
#dictionary
#value can repeat but not key

dic={"ayush":"human","cat":"animal"}
print(dic["ayush"])
print(dic)
print(dic.keys())
print(dic.values())
print(dic.get("cat"))

for key in dic.keys():
    print(f"the values corresponding to the key {key} is {dic[key]}")



print(dic.items())
for key,value in dic.items():
    print(f"the values corresponding to the key {key} is {value}")
