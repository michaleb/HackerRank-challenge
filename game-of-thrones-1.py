import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to print() a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    
    freq_dict = defaultdict(int)
    for x in s:
        freq_dict[x] += 1
            
    freq = 0
    for val in freq_dict.values():
        if val % 2 !=0:
            freq +=1
            if freq > 1:
                print("NO")
    print("YES")

    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    #fptr.write(result + '\n')

    #fptr.close()
