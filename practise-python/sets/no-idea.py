
n, m = map(int, input().split())

arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happy = 0
for ele in arr:
    if ele in a:
        happy = happy + 1
    elif ele in b:
        happy = happy - 1

print(happy)
