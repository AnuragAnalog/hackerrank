#!/usr/bin/python3

from math import sqrt

def roots(a, b, c):
    r1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    r2 = (-b+sqrt(b**2-4*a*c))/(2*a)

    return sorted([r1, r2])

t = int(input())

for i in range(t):
    n = int(input())
    val = roots(1, 1, -2 * n)
    
    if val[1] != int(val[1]):
        print("-1")
    else:
        print(int(val[1]))
