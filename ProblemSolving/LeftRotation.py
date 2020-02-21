#!/bin/python3

import math
import os
import random
import re
import sys

def LeftRotate(arr,n,d):
    b = []
    #arr1 = arr.copy()
    for j in arr[d:]:
        b.append(j)
    for j in arr[:d]:
        b.append(j)
    return b
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    a = LeftRotate(a,n,d)
    for i in a:
        print(i,end=' ')
