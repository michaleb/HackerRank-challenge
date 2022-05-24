#!/bin/python3

from ast import Str
import math
import os
import random
import re
import sys
from collections import defaultdict, deque

from numpy import empty

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Write your code here
    s = sorted(s)
    p = ""
   
    i = 0
    min_cost = 0
    while len(p) < len(s):
        #p.append(s[i])
        
        if p[-1:] == s[i]:
            p = p + p[-1:]
            #print("P-last", p[-1:])
            #
            # print("P-double",p)
        else:
            p = p + s[i]
            min_cost += 1
        #print("P",p)
        #print("S",s[i+1:])
        i +=1       
    
    print(min_cost)    
    
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        #fptr.write(str(result) + '\n')

    #fptr.close()
