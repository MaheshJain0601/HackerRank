#!/bin/python3

'''
https://www.hackerrank.com/challenges/mini-max-sum/problem
'''

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
       total = 0
       arr.sort()
       for i in range(0,5):
              total += arr[i]
       print(total-arr[4],total-arr[0])
              
       
if __name__ == '__main__':
       arr = list(map(int, input().rstrip().split()))

       miniMaxSum(arr)
