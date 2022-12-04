import sys
d = [int(x) for x in sys.stdin]
print(sum([a<b for a, b in zip(d, d[1:])]))