#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     24-06-2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#day 47
#exercise 4 solution

#w.a.p to create a secret code language

st=input("enter message")
words=st.split(" ")
coding=input("1 fro coding or 0 for decoding")
coding==True if (coding=="1") else False
if(coding):
    nwords=[]
    for word in words:
     if (len(word)>=3):
        r1="dgs"
        r2="jko"
        stnew=r1+word[1:]+word[0]+r2
        nwords.append(stnew)
    else:
        nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))