
n = int(input())
arr = list(map(int, input().split()))

mean = round(sum(arr)/n, 1)
tmparr = sorted(arr)
if n%2 == 1:
    median = tmparr[int(n//2)]
else:
    median = round((tmparr[int(n//2)]+tmparr[int(n//2)-1])/2, 2)

if len(set(arr)) == n:
    mode = min(arr)
else:
    maxi = 0
    val = []
    for e in set(arr):
        if arr.count(e) > maxi:
            maxi = arr.count(e)
            val = e
        elif arr.count(e) == maxi:
            if val > e:
                val = e
    mode = val

print(mean)
print(median)
print(mode)
