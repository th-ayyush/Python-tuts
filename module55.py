#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     30-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 60
#getters and setters

#GETTERS
class myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"value is {self._value}")
    @property#getter method
    def ten_value(self):
        return 10*self._value#it is 10 times value of _value
#SETTER
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
        return 10*self._value


obj=myclass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()