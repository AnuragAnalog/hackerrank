
from math import exp

mean = float(input())
x = int(input())

def fact(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)

prob = ((mean**x)*(exp(-1*mean)))/(fact(x))
print(round(prob, 3))
