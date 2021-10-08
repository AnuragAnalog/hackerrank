#! bin/python3

import math

mode = input("What will we use to count area of circle? Length of circumference[l], Radius[r] or Diameter[d]?: ")
if "d" in mode or "D" in mode:
    d = input("What diameter of circle: ")
    s = (math.pi*math.pow(int(d),2))/4
    print("Area of circle is: ", s)
elif "r" in mode or "R" in mode:
    r = input("What radius of circle: ")
    s = math.pi*(math.pow(int(r),2))
    print("Area of circle is:", s)
elif "l" in mode or "L" in mode:
    l = input("What length of circumference: ")
    s = math.pow(int(l),2)/(math.pi*4)
    print("Area of circle is:", s)
else:
    print("Wrong input. Try again")
