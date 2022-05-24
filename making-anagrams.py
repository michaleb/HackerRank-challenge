
import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    
    freq_s1 = defaultdict(int)
    freq_s2 = defaultdict(int)
    
    for char in s1:
        freq_s1[char] +=1
            
    for char in s2:  
        freq_s2[char] +=1  
    
    def string_diff(str1, str2):
        count = 0
        for x in str1:
            freq_s1[x] -= 1
            if x  in str2 and freq_s2[x] >0:
                freq_s2[x] -= 1
            else:
                 count += 1   
        return  sum(freq_s1.values()) + sum(freq_s2.values()) + count 
    
    if len(s1) <= len(s2):
        print(string_diff(s1,s2))
    
    else:
        print(string_diff(s2,s1))
               

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)

    