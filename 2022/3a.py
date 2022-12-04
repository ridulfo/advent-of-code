with open("inputs/day3.txt") as f:
    s = f.read()

print(sum([(ord(set.intersection(set(line[:len(line)//2]), set(line[len(line)//2:])).pop())-38)%58 for line in s.split("\n")]))