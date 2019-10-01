#!/usr/bin/python3

t = int(input())

def fact(n):
    lst = [1,1]
    if n in [0, 1]:
        return lst[n]
    else:
        for i in range(2, n+1):
            lst.append(i*lst[i-1])
    return lst[-1]

for i in range(t):
    num = int(input())

    facts = fact(num)
    s = sum(map(int, list(str(facts))))
    print(s)
