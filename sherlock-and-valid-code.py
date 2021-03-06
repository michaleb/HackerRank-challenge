#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    freq_dict = defaultdict(int) 
    
    for ele in s:
        freq_dict[ele] +=1
    
    count = 0
    once = True
    string_size = len(set(s))
    f_val, _ = Counter(freq_dict.values()).most_common(1)[0]
        
    for val in freq_dict.values():
        if val == f_val :
            count+=1
        else:
            if (val - 1 == f_val or val - 1 == 0) and once: 
                once = False
                count +=1 
            if val + 1 == f_val and once:  
                once = False
                count +=1 
            
    if count == string_size :
        print("YES")  
    else:
        print("NO")
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    #fptr.write(result + '\n')

    #fptr.close()
