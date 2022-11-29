import sys

l = next(sys.stdin)
print(l.count("(")-l.count(")"))