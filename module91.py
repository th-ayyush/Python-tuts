#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     01-09-2024
# Copyright:   (c) User 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

A="OOTD.YOLO.ASAP.BRB.GTG.OTW"

words = A.split('.')

comma_separated_values = ",".join(words)


print(comma_separated_values)

words_sorted=sorted(A)
print(words_sorted)

Z="F.R.I.E.N.D.S"

char_to_remove = '.'

result = Z.replace(char_to_remove, "")

print(result)

