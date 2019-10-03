
from itertools import permutations

l = input().split()

s = l[0]
n = int(l[1])

gen = permutations(s, n)

m = list(map("".join, gen))
m.sort()
for i in m:
    print(i)