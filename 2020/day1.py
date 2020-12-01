def readReport():
    with open("inputDay1.txt") as f:
        return [int(x) for x in f.read().split("\n") if x != ""]

def part1():
    report = readReport()
    for a in report:
        for b in report:
            if a+b==2020:
                return a*b

def part2():
    report = readReport()
    for a in report:
        for b in report:
            for c in report:
                if a+b+c==2020:
                    return a*b*c

print(part1())
print(part2())
