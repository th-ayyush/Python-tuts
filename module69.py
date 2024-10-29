#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      User
#
# Created:     02-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 74
#method overriding


class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
rec=shape(3,5)
print(rec.area())

#now we want to find the area of circle
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self):
        return 3.14*super().area()
        #return 3.14*self.radius*self.radius

c=circle(5)
print(c.area())