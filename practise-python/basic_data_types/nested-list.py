
n = int(input())

arr = list()
names = list()
marks = list()
for i in range(n):
    name = input()
    names.append(name)
    mark = float(input())
    marks.append(mark)
    arr.append([name, mark])
marks.sort()
m = marks[0]
c = marks.count(m)
for i in range(c):
    marks.remove(m)
m = min(marks)

l = list()
for i in range(n):
    if arr[i][1] == m:
        l.append(arr[i][0])
for name in sorted(l):
    print(name)
