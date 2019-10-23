
n = int(input())
arr = list(map(int, input().split()))
freq = list(map(int, input().split()))

def median(arr, n):
    if n%2 == 1:
        return arr[int(n//2)]
    else:
        return (arr[int(n//2)]+arr[int(n//2)-1])/2

def quartile(arr, n):
    if n%2 == 1:
        q2 = arr[int(n//2)]
        tmp = arr[:int(n//2)]
        q1 = median(tmp, len(tmp))
        tmp = arr[int(n//2)+1:]
        q3 = median(tmp, len(tmp))
    else:
        q2 = median(arr, n)
        tmp = arr[:int(n//2)]
        q1 = median(tmp, len(tmp))
        tmp = arr[int(n//2):]
        q3 = median(tmp, len(tmp))
    return q1, q2, q3

tmp = []
for i in range(n):
    tmp.extend([arr[i]]*freq[i])
tmp.sort()
q1, q2, q3 = quartile(tmp, len(tmp))
print(round(float(q3-q1), 1))
