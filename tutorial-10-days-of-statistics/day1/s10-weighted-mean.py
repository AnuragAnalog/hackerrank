
n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

num = 0
dem = 0
for i in range(n):
    num = num + (x[i]*w[i])
    dem = dem + w[i]
mw = round(num/dem, 1)
print(mw)
