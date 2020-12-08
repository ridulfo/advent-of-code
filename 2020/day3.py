from functools import reduce 

def getMap():
    with open("inputDay3.txt", "r") as f:
        return [list(line) for line in f.read().strip().split("\n")]

def part1():
    slope = (3,1)
    count = 0
    for i, line in enumerate(getMap()):
        if line[(i*slope[0])%len(line)]=="#":
            count += 1
    return count

def part2():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    counts = []
    m = getMap()
    for slope in slopes:
        count = 0
        x = 0
        for i in range(0, len(m), slope[1]):
            if m[i][x%len(m[i])]=="#":
                count += 1
            x+=slope[0]
        counts.append(count)
    return reduce((lambda x, y: x*y), counts)

print(part1())
print(part2())
