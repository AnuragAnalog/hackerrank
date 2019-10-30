from math import sqrt

n = 100
mean = 500
sd = 80 / sqrt(n)

A = (-1.96*sd)+mean
B = (1.96*sd)+mean
print(A)
print(B)
