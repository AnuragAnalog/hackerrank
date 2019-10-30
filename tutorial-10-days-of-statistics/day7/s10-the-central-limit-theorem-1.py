from math import erf, sqrt

capacity = 9800
boxes = 49
mean = 205 * boxes
sd = 15 * sqrt(boxes)

val1 = (1+erf((capacity-mean)/(sd*sqrt(2))))/2
print(round(val1, 4))
