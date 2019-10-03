
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for x in product(a, b):
    print(x, end = " ")
print("")