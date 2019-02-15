#!/bin/python3

import math
import os
import random
import re
import sys
#import numpy as np
#
# Complete the 'numbersSquare' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER s
#

def numbersSquare(n, s):
    # Write your code here
    #rs = [[0,0],[0,0]]
    rs = [[0 for j in range(n)] for i in range(n)]
    #rs = np.zeros(n,n)
    for i in range (0,n):
        if i==0:
            rs[0][0]=s
        else:
            data = rs[i-1][0]
            for j in range (0,i+1):
                data+=1
                #rs[j][i].append(data)
                rs[j][i]=data
            for j in range(i-1,-1,-1):
                rs[i][j] = rs[i][j+1]+1
    for i in range(0,n):
        str1 = ' '.join(map(str,rs[i]))     #------> HOW TO PRINT LIST AS STRING
        print(str1)
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    s = int(first_multiple_input[1])

    numbersSquare(n, s)
