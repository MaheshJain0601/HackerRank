#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(N, K, Array):
    count=0
    for i in range(N):
        for j in range(i+1,N):
            if (Array[i]+Array[j])%k==0:
                count+=1
            
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
