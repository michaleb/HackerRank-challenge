#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    a = n//c
    b = a//m
    d = b//m
    return (a + b + d + (a%m + b%m + d%m)//m) 
    
if __name__ == '__main__':
    fptr = open('cho-feast.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        #print(result,'\n')
        fptr.write(str(result) + '\n')
    
    fptr.close()
