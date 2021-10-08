#! bin/python3

import math

a = int(input())
b = int(input())
print(round(math.degrees(math.acos(b/pow((a**2) + (b**2),1/2)))),'°',sep="")
