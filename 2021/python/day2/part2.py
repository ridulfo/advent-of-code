import sys

h=d=aim=0
for a, b in map(str.split, sys.stdin):
    if "f" in a:
        h += int(b)
        d += int(b)*aim
    elif a == "down": aim += int(b)
    elif a == "up": aim -= int(b)

print(h*d)