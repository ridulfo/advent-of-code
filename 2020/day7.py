from time import sleep

def getrules():
    with open("inputDay7.txt", "r") as f:
        rules = dict()
        for line in f.read().strip().split("\n"):
            line = line.replace(" bags", "")
            line = line.replace(" bag", "")
            line = line.replace(".", "")
            main, contains = line.split(" contain ")
            rules[main] = list()
            if "other" not in contains:
                for rule in contains.split(", "):
                    n, color = rule.split(" ", 1)
                    rules[main].append((int(n), color))
        return rules
                
def part1():
    rules = getrules()
    def recsearch(rules, bag):
        if bag=="shiny gold": return True
        return any((recsearch(rules, nextBag[1]) for nextBag in rules[bag]))
    return sum((1 if recsearch(rules, bag) else 0 for bag in rules))-1

def part2():
    rules = getrules()
    def recsearch(rules, parentBag):
        if len(rules[parentBag])==0: return 1
        return sum([num*recsearch(rules, bag) for num, bag in rules[parentBag]])+1
    return recsearch(rules, "shiny gold")-1

print(part1())
print(part2())
