
from itertools import combinations

l = input().split()

s = l[0]
n = int(l[1])

for j in range(1, n+1):
    gen = combinations(s, j)
    
    m = list()
    for x in gen:
        m.append("".join(sorted(x)))
    m.sort()
    for i in m:
        print(i)