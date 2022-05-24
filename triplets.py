#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys


'''
So the code is tracking potential pairs and triplets as it walks through the array.

For each value in the array:
    * Increment count by the number of triplets that end with k
        count += triplets[k]
    * Increment the number of potential triplets that will end with k*r
        triplets[k*r] += pairs[k]
    * Increment the number of potential pairs that end with k*r
        pairs[k*r] += 1  
The number of triplets for any given k is the number of pairs for any given k/r that we've
encountered up to this point. Note throughout the loop, triplets[k] and pairs[k] will often be zero,
until they hit our predicted k*r value from a previous iteration.

'''

# Complete the countTriplets function below.
def countTriplets(arr, r):    
    pairs = defaultdict(int)
    triplets = defaultdict(int)
    count = 0
    for k in arr:
        count += triplets[k]
        print("Count", count)
        triplets[k*r] += pairs[k]
        print("triplets",triplets)
        pairs[k*r] += 1
        print("pairs", pairs)
    return count 
        
        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    #fptr.write(str(ans) + '\n')

    #fptr.close()
