#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    s = deque(s)
    pal = ""
    def isPalindrome(s):
        diff = 0
        i = 0
        j = n-1
        while j > i:
            if s[i] != s[j]:
                diff += 1 
            i+=1
            j-=1
        return diff   

    def maxPalindrome(s,k):
        i = 0
        j = n-1
        
        while j >= i:
            if k>=2:
                if s[i] != '9':
                    s[i] = '9'
                    s[j] = s[i]
                    k-=2                 
            else:
                if k == 1 and (n-1)%2 ==0:
                    s[(n-1)//2] = '9'
                    break
            i+=1
            j-=1
    
        return s
    
    def makePalindrome(s, diff_str, k):
        i = 0
        j = n-1
        
        while j > i and k > 0:
            if s[i] == s[j]:
                if k > diff_str + 1 and s[i] != '9':
                    s[i] = '9'
                    s[j] = s[i]
                    k -=2
            else:
                if s[i] == '9':
                    s[j] = '9'
                    diff_str -= 1
                    k -=1
                    
                elif s[j] == '9':
                    s[i] = '9'
                    diff_str -= 1
                    k -=1               
                
                else:
                    if k >= diff_str + 1:
                        s[i] = '9'
                        s[j] = s[i]
                        diff_str -= 1
                        k -=2
                    else:
                        if s[i] > s[j]:
                            s[j] = s[i]
                        else:
                            s[i] = s[j]
                        diff_str -= 1
                        k -=1
            i+=1
            j-=1
        
        return maxPalindrome(s,k)

    diff_str = isPalindrome(s)
    
    if diff_str > k:
        print("-1")
            
    else:
        pal = makePalindrome(s, diff_str,k)
        print(''.join(pal))
    
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    #fptr.write(result + '\n')

    #fptr.close()