# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:06:30 2019

@author: utkarsh
"""
"""Day0 : Mean Median Mode"""
import numpy as np

n = int(input().strip())

​

numbers = list(map(int , input().split()))

​

print(np.mean(numbers))

print(np.median(numbers))

from scipy.stats import mode

print(int(mode(numbers)[0]))

"""Day0: Find Weighted mean"""


n = int(input().strip())

numbers = list(map(int, input().split()))
freq = list(map(int, input().split()))
weightedmean = 0.0
count = 0

weightedmean = sum([a*b for a,b in zip(numbers,freq)])
weightedmean = round((weightedmean/sum(freq)),1)
print(weightedmean)
    
