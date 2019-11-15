
n, m = map(int, input().split())

for i in range(0,n-2,2):
    s = '.|.'*(i+1)
    print(s.center(m, '-'))
print("WELCOME".center(m, '-'))
for i in range(n-2, 0, -2):
    s = '.|.'*(i)
    print(s.center(m, '-'))
