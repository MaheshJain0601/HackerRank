#!/bin/python3
'''
Kangaroo Hackerrank SOlution in python
https://www.hackerrank.com/challenges/kangaroo/problem
'''

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
           if v2>v1 and x2>x1 :
                  return "NO"
           else:
                  pass
if __name__ == '__main__':
           #fptr = open(os.environ['OUTPUT_PATH'], 'w')

           x1V1X2V2 = input().split()

           x1 = int(x1V1X2V2[0])

           v1 = int(x1V1X2V2[1])

           x2 = int(x1V1X2V2[2])

           v2 = int(x1V1X2V2[3])

           result = kangaroo(x1, v1, x2, v2)

           #fptr.write(result + '\n')

           print(result + '\n')
           
           #fptr.close()
