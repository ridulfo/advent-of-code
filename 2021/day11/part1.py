ex = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
ex = """11111
19991
19191
19991
11111"""

m = [[int(cell) for cell in line] for line in ex.split('\n')]  # [y][x]
print("\n".join(str(l) for l in m))
print()
for it in range(3):
    m = [[cell+1 for cell in row] for row in m]
    while any(any(cell>9 for cell in row) for row in m):
        for y in range(len(m)):
            for x in range(len(m[y])):
                if m[y][x] > 9:
                    m[y][x] = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            try:
                                m[y+dy][x+dx] += 1
                            except IndexError:
                                pass
    print("\n".join(str(l) for l in m))
    print()
                
print()
print("\n".join(str(l) for l in m))
