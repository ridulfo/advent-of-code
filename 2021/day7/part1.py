import sys
ex = list(map(int, sys.stdin.read().split(",")))
print(min([sum([abs(pos-x) for x in ex]) for pos in range(max(ex) + 1)]))
