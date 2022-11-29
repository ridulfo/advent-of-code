import sys

field = {}
for line in sys.stdin:
    a, b = line.split(' -> ')
    a, b = tuple(map(int, a.split(','))), tuple(map(int, b.split(',')))
    while True:
        if a not in field: field[a] = 0
        field[a] += 1
        if a==b: break
        x = 0 if a[0]==b[0] else (1 if a[0] < b[0] else -1)
        y = 0 if a[1]==b[1] else (1 if a[1] < b[1] else - 1)
        a = (a[0] + x, a[1] + y)
print(len([x for x in field.values() if x>1]))