#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     17-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#day16
#match case statement

x=int(input("enter the value of x"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")

    #it is default value :_
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)
