#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
        
    if s[-2:] == 'PM':
        
        if int(s[:2]) != 12:
            
            hr = str(int(s[:2])+12) 
        else:
            hr = '12'
    else:
        if int(s[:2]) == 12 :
            hr = '00' 
        else:
            if len(s[:2]) < 2:
                hr = '0' + s[:2]
            else:
                hr = s[:2]
    
    time_slice = s[2:-2]
    print('{}{}'.format(hr, time_slice))           
       
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print('Please enter time to be converted')
    s = input()
    while len(s)<10:
        print('Time format must be "hh:mm:ssXX" XX = AM/PM')
        s = input()

    result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()