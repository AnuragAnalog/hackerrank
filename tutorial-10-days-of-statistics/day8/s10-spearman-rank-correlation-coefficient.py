
def spearman_correlation(x, y, n):
    tmpx = sorted(x)
    tmpy = sorted(y)
    num = 0
    for i in range(n):
        rx = tmpx.index(x[i])
        ry = tmpy.index(y[i])
        num = num + (rx-ry)**2
    corr = 1-((6*num)/(n*(n**2-1)))
    return corr

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

corr = spearman_correlation(x, y, n)
print(round(corr, 3))

