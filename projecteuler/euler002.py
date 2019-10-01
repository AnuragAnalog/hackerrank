#!/bin/python3

import sys


t = int(input().strip())
for n in range(t):
    num = int(input(""))
    a = 1
    b = 2
    tot = 0
    while a < num:
        if a%2 == 0:
            tot = tot + a
        c = a + b
        a = b
        b = c
    print(tot)
