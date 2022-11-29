import sys
print(sum([2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l) for l, w, h in [map(int, l.split("x")) for l in sys.stdin]]))