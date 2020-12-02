def getPass():
    with open("inputDay2.txt", "r") as f:
        lines = list()
        for row in f.read().strip().split("\n"):
            line = list()
            parts = row.split(" ")
            line += [int(num) for num in parts[0].split("-")]
            line.append(parts[1][:-1])
            line.append(parts[2])
            lines.append(line)
        return lines

def part1():
    count = 0
    for line in getPass():
        c = len(line[3]) - len(line[3].replace(line[2], ""))
        if c>=line[0] and c<=line[1]:
            count+=1
    return count

def part1Mini():
    return sum((1 for line in getPass() if len(line[3]) - len(line[3].replace(line[2], "")) in range(line[0], line[1]+1)))

def part2():
    count = 0
    for line in getPass():
        if sum([1 for pos in line[0:2] if line[3][pos-1]==line[2]])==1:
            count+=1
    return count

def part2Mini():
    return sum(( 1 for line in getPass() if sum(((line[3][pos-1]==line[2])==1 for pos in line[0:2]))==1))

print(part1())
print(part1Mini())
print(part2())
print(part2Mini())

from day1 import timeit
timeit(part1)
timeit(part1Mini)
timeit(part2)
timeit(part2Mini)

