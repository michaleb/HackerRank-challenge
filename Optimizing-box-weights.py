#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    # Write your code here
    arr = sorted(arr)
    #print("1", arr)
    #arr_length = len(arr)
    arr_A = []
    #arr_sum = sum(arr)
    
    while sum(arr) > sum(arr_A):
        arr_A.append(arr[-1])
        arr = arr[:-1]
        print(arr)
        print(arr_A)
    
    return sorted(arr_A)    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minimalHeaviestSetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
