#Finding linear equations

n = int(input())
arr = [int(i) for i in input().split()][:n*2]
mydic = {}
flag = 0
for i in arr:
    if i not in mydic:
        mydic[i] = 1
    else:
        mydic[i] += 1
for i in mydic:
    if mydic[i] == 2:
        flag = 1
    else:
        flag = 0
        break
if flag:
    print(str(arr[2]-arr[0])+'x-'+str(arr[5]-arr[3])+'y=0')
else:
    print(0)