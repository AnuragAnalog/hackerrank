
m1, m2 = map(float, input().split())

ca = 160 + 40*(m1+m1**2)
cb = 128 + 40*(m2+m2**2)
print(round(ca, 3))
print(round(cb, 3))
