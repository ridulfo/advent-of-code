import sys

a, b = list(zip(*[x.split("|") for x in sys.stdin.read().split('\n')]))
b = sum([1 for x in [x.split() for x in b] for y in x if len(y) in [2, 4, 3, 7]])
print(b)