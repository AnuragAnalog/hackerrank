
n = int(input())

lt = list()
for i in range(n):
    l = list(input().split())
    lt.append(l)
name = input()
avg = 0
for i in range(n):
    if lt[i][0] == name:
        avg = sum(list(map(float, lt[i][1:])))/(len(lt[i])-1)
        break
print("%.2f"%round(avg, 2))
