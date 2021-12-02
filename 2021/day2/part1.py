import sys

d = h = 0
for a, b in map(str.split, sys.stdin):
    if "f" in a:   h += int(b)
    elif "d" in a: d += int(b)
    elif "u" in a: d -= int(b)
print(d*h)
