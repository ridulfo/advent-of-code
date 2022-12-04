with open("inputs/day1.txt") as f:
    s = f.read()

print(max([sum(map(int, e.split("\n"))) for e in s.split("\n\n")])) 