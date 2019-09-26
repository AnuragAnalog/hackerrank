
k = int(input())
arr = list(map(int, input().split()))

# Here simply we duplicate the number of captian rooms and the we divide them
sum1 = sum(arr)
sum2 = sum(set(arr))*k
print(int((sum2-sum1)/(k-1)))
