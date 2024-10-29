#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      User
#
# Created:     02-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 73-did not understand
#Magic and dunder methods in python
# which starts with double underscore and end with double score


class employee:
    name="ayush"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return 1
e=employee()
print(e.name)
print(len(e))