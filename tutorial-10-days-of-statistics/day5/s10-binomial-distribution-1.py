
def fact(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)

def c(n, r):
    return fact(n)/(fact(n-r)*fact(r))

x, y = map(float, input().split())
p = x/(x+y)

n = 6
tot = 0
for r in range(3, 7):
    tot = tot + (p**r)*((1-p)**(n-r))*c(n,r)
print(round(tot, 3))
