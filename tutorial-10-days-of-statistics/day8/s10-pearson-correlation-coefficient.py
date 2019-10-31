
def pearson_corelation(x, y, n):
    mux = sum(x)/n
    muy = sum(y)/n
    num = 0
    sdx = 0
    sdy = 0
    for i in range(n):
        sdx = sdx + ((x[i]-mux)**2)
        sdy = sdy + ((y[i]-muy)**2)
        num = num + (x[i]-mux)*(y[i]-muy)
    sdx = (sdx/n)**0.5
    sdy = (sdy/n)**0.5
    corr = (num)/(n*sdx*sdy)
    return corr

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

corr = pearson_corelation(x, y, n)
print(round(corr, 3))

