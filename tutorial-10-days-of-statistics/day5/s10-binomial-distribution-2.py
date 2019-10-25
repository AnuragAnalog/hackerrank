
def fact(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)

def c(n, r):
    return fact(n)/(fact(n-r)*fact(r))

p, n = map(int, input().split())
p = p/100

tot = 0
for r in range(0, 3):
    tot = tot + (p**r)*((1-p)**(n-r))*c(n,r)
print(round(tot, 3))

tot = 0
for r in range(2, n+1):
    tot = tot + (p**r)*((1-p)**(n-r))*c(n,r)
print(round(tot, 3))

