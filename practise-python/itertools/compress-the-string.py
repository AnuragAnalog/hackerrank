
from itertools import groupby

string = input()
out = ""

for k, g in groupby(string):
    out = out + str((len(list(g)), int(k))) + " "
print(out[:-1])

