import collections
n = int(input())
d = collections.OrderedDict()

for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print (len(d))
for key, value in d.items():
    print (value,end=' ')
    

