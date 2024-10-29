#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     01-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 67
#EXERCISE 6 SOLUTION

class library:
    def __init__(self):
        self.nobooks=0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def showinfo(self):
     print(f"the library has {self.nobooks}books.The books are")
     for book in self.books:
        print(book)


l1=library()
l1.addbook("harry potter")
l1.addbook("fifty shades of gray")
l1.addbook("the room 141")
l1.showinfo()