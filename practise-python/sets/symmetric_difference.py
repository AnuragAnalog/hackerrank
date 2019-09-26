
n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

t1 = s1.difference(s2)
t2 = s2.difference(s1)
s3 = t1.union(t2)

s3 = sorted(s3)
for ele in s3:
    print(ele)
