def getAns():
    with open("inputDay6.txt", "r") as f:
        groups = list()
        for group in f.read().strip().split("\n\n"):
            groups.append([[char for char in pers] for pers in group.split("\n")])
        return groups

def part1():
    count = 0
    for group in getAns():
        ans = set()
        for pers in group:
            ans.update(pers)
        count+=len(ans)
    return count

def part2():
    count = 0
    for group in getAns():
        ans = set(group[0])
        for pers in group[1:]:
            ans = ans.intersection(pers)
        count+=len(ans)
    return count

print(part1())
print(part2())

