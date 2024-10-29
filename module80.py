#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     06-07-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#DAY 85
#COMMAND LINE UTILITY
#THEY ARE PROGRAMS THAT CAN BE RUN FROM TERMINAL

import argparse
parser=argparse.ArgumentParser()

#add command line arguments
parser.add_argument("url",help="url of the file to download")
parser.add_argument("output",help="by which name do you want to save your file")

#parse the arguments
args=parser.parse_args()

#use the arguments in your code
print(args.url)
print(args.output)

#NOTE-checkout stackoverflow