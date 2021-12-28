#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum=0
    max=-999
    for i in range(0,4):
        for j in range(0,4):
            sum+=arr[j][i]
            print(arr[j][i],end='')
            sum+=arr[j][i+1]
            print(arr[j][i+1],end='')
            sum+=arr[j][i+2]
            print(arr[j][i+2])
            
            sum+=arr[j+1][i+1]
            print(arr[j+1][i+1])
            
            sum+=arr[j+2][i]
            print(arr[j+2][i],end='')
            sum+=arr[j+2][i+1]
            print(arr[j+2][i+1],end='')
            sum+=arr[j+2][i+2]
            print(arr[j+2][i+2])
            print(sum)
            
            if sum>max:
                max=sum
            sum=0
    print(-6>-19)
    return max
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
