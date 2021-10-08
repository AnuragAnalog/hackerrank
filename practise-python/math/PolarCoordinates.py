#! bin/python3

from cmath import phase

n = complex(input())


print(abs(n))

print(phase(complex(n.real,n.imag)))
