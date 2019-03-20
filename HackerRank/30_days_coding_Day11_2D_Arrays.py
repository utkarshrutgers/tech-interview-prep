#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    a = 0
    
    #sumarr = []
    maxn = None
    for i in range(len(arr)- 2):
        for j in range(len(arr)- 2):
            
            sumn = 0
            for k in range(0,3):
                
                if(k==1):
                    sumn = sumn + arr[i+k][j+k]
                else:
                    sumn = sumn + arr[i+k][j] + arr[i+k][j+1]+arr[i+k][j+2]
            if  maxn==None or sumn > maxn:
                maxn = sumn          
            #sumarr.append(sumn)
            
    #print(max(sumarr))
    print(maxn)
                    


   
