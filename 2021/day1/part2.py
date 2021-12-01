import sys
d = [int(x) for x in sys.stdin]
s = [sum(x) for x in zip(d, d[1:], d[2:])]
print(sum([a<b for a, b in zip(s, s[1:])]))