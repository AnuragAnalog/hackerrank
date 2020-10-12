import math
AB=int(input())
BC=int(input())
AC=math.sqrt(pow(AB,2)+pow(BC,2))
MC=AC/2
adj=BC/2
print(str(int(round(math.degrees(math.acos(adj/MC))))) + "°")

