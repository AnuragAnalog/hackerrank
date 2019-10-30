
from math import erf, sqrt

mean, sd = 20, 2
x1 = 19.5
x2, x3 = 20, 22

val1 = (1+erf((x1-mean)/(sd*sqrt(2))))/2
val2 = (1+erf((x3-mean)/(sd*sqrt(2))))/2 - (1+erf((x2-mean)/(sd*sqrt(2))))/2
print(val1)
print(val2)

