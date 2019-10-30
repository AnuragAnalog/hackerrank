
from math import erf, sqrt

mean, sd = 70, 10
x1 = 80
x2 = 60

val1 = 1 - ((1+erf((x1-mean)/(sd*sqrt(2))))/2)
val2 = 1 - ((1+erf((x2-mean)/(sd*sqrt(2))))/2)
val3 = (1+erf((x2-mean)/(sd*sqrt(2))))/2
print(round(val1*100, 2))
print(round(val2*100, 2))
print(round(val3*100, 2))
