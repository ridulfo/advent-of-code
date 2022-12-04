import sys

i = sys.stdin.read().split("\n")
c = [0]*len(i[0])
for l in i:
    for ix, b in enumerate(l):
        c[ix]+=int(b)

g = int("".join("1" if b/len(i)>0.5 else "0" for b in c),2)
e = int("".join("0" if b/len(i)>0.5 else "1" for b in c),2)
print(g*e)