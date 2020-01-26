#!/bin/python3

'''
https://www.hackerrank.com/challenges/staircase/problem
'''

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(0,n):
        j=n-i-1
        #print(j)
        while j!=0:
            print(" ",end='')
            j-=1
        j=i+1
        while j!=0:
            print('#',end='')
            j-=1
        print("")
        
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
