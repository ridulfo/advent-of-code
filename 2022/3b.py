with open("inputs/day3.txt") as f:
    s = f.read()

print(sum([(ord(set.intersection(*map(set, lines)).pop())-38)%58 for lines in [s.split("\n")[i:i+3] for i in range(0, len(s.split("\n")), 3)]]))