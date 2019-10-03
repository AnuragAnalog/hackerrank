#!/bin/python3

t=int(input())

for i in range(t):
    n =int(input())

    num = str(2**n)
    sum_dig = sum(map(int, list(num)))
    print(sum_dig)
