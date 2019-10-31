
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

t1 = t2 = 0
for i in range(5):
    t1 = t1 + x[i]*y[i]
    t2 = t2 + x[i]*x[i]
m = (t1 - sum(x)*sum(y))/(t2 - sum(x)**2)
c = (sum(y) - m*sum(x))

yhat = m * 80 + c
print(round(yhat, 3))

