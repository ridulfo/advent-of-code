def getjolts():
    with open("input10.txt", "r") as f:
        l = [int(x) for x in f.read().strip().split("\n")]
        l+=[0, max(l)+3]
        l.sort()
        return l

def part1():
    jolts = getjolts()
    diffs=[j-i for i, j in zip(jolts[:-1], jolts[1:])]
    return len([1 for x in diffs if x==1])*len([1 for x in diffs if x==3])

def part2():
    jolts = getjolts()
    dev = max(jolts)
    def rec(currjolt, count):
        if currjolt==dev: #arrived
            return count+1
        for jolt in [j for j in jolts if j>currjolt and j<currjolt+4]:
            count=rec(jolt, count)
        return count
    
    return rec(0, 0)

def part2b():
    jolts = getjolts()
    cache = {0:1}
    for jolt in jolts[1:]:
        cache[jolt] = cache.get(jolt-1,0)+cache.get(jolt-2,0)+cache.get(jolt-3,0)
    return cache[jolts[-1]]

print(part1())
#print(part2())
print(part2b())
