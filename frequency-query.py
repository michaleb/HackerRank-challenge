#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

from numpy import array_split

# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    array = defaultdict(int)
        
    for query in queries:
        operator = query[0]
        data_element = query[1]
        
        if operator == 1:
            array[data_element] += 1
         
        elif operator == 2:
            if data_element in array and array[data_element] > 0:
                array[data_element] -= 1
                
        else:
            output.append(1 if data_element in set(array.values()) else 0)
                    
    return output                    
     
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)

    #fptr.write('\n'.join(map(str, ans)))
    #fptr.write('\n')

    #fptr.close()
