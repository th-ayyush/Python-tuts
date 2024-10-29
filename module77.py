#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     04-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 82
#EXERCISE 8 SOLUTION
#MERGE PDF

from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()