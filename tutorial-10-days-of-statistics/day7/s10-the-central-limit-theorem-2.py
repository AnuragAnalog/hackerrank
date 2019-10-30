from math import erf, sqrt

capacity = 250
boxes = 100
mean = 2.4 * boxes
sd = 2.0 * sqrt(boxes)

val1 = (1+erf((capacity-mean)/(sd*sqrt(2))))/2
print(round(val1, 4))
