#!/bin/python3
'''
Time Conversion hackerrank solution in python
https://www.hackerrank.com/challenges/time-conversion/problem
'''

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
           # Write your code here.
           hour = int(s[0:2])
           if s[8:10] == "AM" :
                  if hour == 12:
                         return "00"+s[2:8]
                  else:
                         return s[:8]
           elif s[8:10] == "PM":
                  if hour == 12:
                         return s[:8]
                  else:
                         return str(12+hour)+s[2:8]
           
if __name__ == '__main__':
           #f = open(os.environ['OUTPUT_PATH'], 'w')

           s = input()

           result = timeConversion(s)

           #f.write(result + '\n')
           print(result + '\n')

           #f.close()
