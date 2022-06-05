 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'morganAndString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def morganAndString(a, b):
    # Write your code here
    a += 'z'
    b += 'z'
    upper_str =""
    
    for _ in range(len(a)+len(b)-2):
        if a <= b:
            upper_str += a[0]
            a = a[1:]
            
        else:
            upper_str += b[0]
            b = b[1:]
                        
    upper_str += a[: -1] + b[:-1]
    
    return upper_str

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        print(morganAndString(a, b))

        #fptr.write(result + '\n')

    #fptr.close()
