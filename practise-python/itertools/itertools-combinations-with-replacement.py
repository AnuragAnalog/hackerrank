
from itertools import combinations_with_replacement

inp = input().split()

word = inp[0]
n = int(inp[1])

comb = combinations_with_replacement(word, n)

lt = list()
for val in comb:
    lt.append("".join(sorted(val)))
lt.sort()

for val in lt:
    print(val)
