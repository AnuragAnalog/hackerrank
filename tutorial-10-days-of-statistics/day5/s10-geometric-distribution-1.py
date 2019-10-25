
num, dem = map(int, input().split())
n = int(input())

p = num/dem
prob = (1-p)**(n-1)*p
print(round(prob, 3))
