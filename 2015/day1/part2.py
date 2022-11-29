import sys
a = 0
for i, c in enumerate(next(sys.stdin)):
    a+=[-1,1][c=='(']
    if a < 0: break
print(i+1)