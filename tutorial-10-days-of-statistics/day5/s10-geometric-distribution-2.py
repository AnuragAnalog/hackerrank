
num, dem = map(int, input().split())
n = int(input())

p = num/dem
prob = 0
for i in range(1, n+1):
    prob = prob + (1-p)**(i-1)*p
print(round(prob, 3))
