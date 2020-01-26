#!/bin/python3
'''
Birthday Cake Candles hackerrank solution in python
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
            maximum = max(ar)
            count = ar.count(maximum)
            return count

if __name__ == '__main__':
           #fptr = open(os.environ['OUTPUT_PATH'], 'w')

           ar_count = int(input())

           ar = list(map(int, input().rstrip().split()))

           result = birthdayCakeCandles(ar)

           print(str(result) + '\n')

           #fptr.close()
