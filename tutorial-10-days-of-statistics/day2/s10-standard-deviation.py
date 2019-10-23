
from math import sqrt

n = int(input())
arr = list(map(int, input().split()))

def std_dev(arr, n):
    mean = sum(arr)/n
    tmp = 0
    for i in range(n):
        tmp = tmp + (arr[i]-mean)**2
    tmp = tmp/n
    tmp = sqrt(tmp)
    return tmp

sd = std_dev(arr, n)
print(round(float(sd), 1))
