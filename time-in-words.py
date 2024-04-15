#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    minutedict = {0:"o' clock", 1:'one', 2:'two', 3:'three',
               4:'four', 5:'five', 6:'six', 7:'seven', 
               8:'eight', 9:'nine', 10:'ten', 11:'eleven', 
               12:'twelve', 13:'thirteen', 15:'quarter', 
               20:'twenty', 30:'half'}
                   
    mins_in_hr = 60
    phrase = [" past "," to ", " minute", " minutes"]

    if h > 12:
        h = h%12
    
    if m == 0:
       minute = minutedict[0]
       print(minutedict[h]+" "+minutedict[0])
       return
    
    elif m <= 30:
        joiner = phrase[0] 
        
    else:
        joiner = phrase[1] 
        h = h%12 + 1       
        m = mins_in_hr - m       
        
    if m == 15 or m == 30:
        minute = minutedict[m]
    elif m==1:
        minute = minutedict[m]+phrase[2]    
    elif m <= 13 or m == 20:
            minute = minutedict[m]+phrase[3]
    elif m > 20:
            minute = minutedict[20]+" "+ minutedict[m-20]+phrase[3]  
    elif m > 13:
            minute =  minutedict[m-10]+"teen"+phrase[3]

    hour = minutedict[h]  
    
    print(minute + joiner + hour)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    '''fptr.write(result + '\n')

    fptr.close()'''
