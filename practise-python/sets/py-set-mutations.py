
n = int(input())
initarr = set(map(int, input().split()))

t = int(input())

for i in range(t):
    oper = input().split()
    tmparr = set(map(int, input().split()))
    if oper[0] == "update":
        initarr.update(tmparr)
    elif oper[0] == "intersection_update":
        initarr.intersection_update(tmparr)
    elif oper[0] == "symmetric_difference_update":
        initarr.symmetric_difference_update(tmparr)
    elif oper[0] == "difference_update":
        initarr.difference_update(tmparr)
print(sum(initarr))
