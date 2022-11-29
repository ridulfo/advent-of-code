import sys
ex = list(map(int, sys.stdin.read().split(",")))
eq = lambda x: 0.5*x**2 + 0.5*x
print(int(min([sum([eq(abs(pos-x)) for x in ex]) for pos in range(max(ex) + 1)])))
