#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    n=len(arr)

    dp=[0 for i in range(n+1)]
    dp1=[0 for i in range(n+1)]

    for i in range(1,n+1):
        a=arr[i-1]+dp[i-1]
        b=dp[i-1]
        a1=arr[i-1]+dp1[i-1]
        b1=0
        dp[i]=max(a,b)
        dp1[i]=max(a1,b1)
    r=max(dp1)
    s=max(dp)
    if r==0:
        r=s=max(arr)
    return r,s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
