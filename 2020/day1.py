from time import time

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

def timeit(func):
    t0 = time()
    result = func()
    t1 = time()
    print("Answer:", result, "Time:", round((t1-t0)*1000, 2), "ms")

if __name__ == "__main__":
    timeit(part1)
    timeit(part2)
