import copy

def getIn():
    with open("input14.txt", "r") as f:
        lines = list()
        for line in f.read().strip().split("\n"):
            line = line.split(" = ")
            if "mask" in line[0]:
                lines.append(line)
            else:
                lines.append(line[0].replace("]","").split("[")+[line[1]])
        return lines

def part1():
    mem = dict()
    bitmask = dict()
    for line in getIn():
        if line[0] == "mask":
            bitmask.clear()
            bitmask.update((i,val) for i, val in enumerate(line[1]) if val!="X")
        else:
            val = list(bin(int(line[2]))[2:].zfill(36))
            for k,w in bitmask.items(): val[k] = w
            mem[line[1]] = "".join(val)
    return sum((int(x,2) for x in mem.values()))
        
def part2():
    mem = dict()
    for line in getIn():
        if line[0] == "mask":
            bitmask = line[1]
        else:
            val = list(bin(int(line[1]))[2:].zfill(36))
            for i, bit in enumerate(bitmask): 
                if bit in "X1": val[i] = bit #Apply mask
            val = "".join(val)
            done, constructing = list(), [val]
            while len(constructing)>0:
                addr = constructing.pop()
                if "X" not in addr:
                    done.append(addr)
                else:
                    constructing += [addr.replace("X","0",1),addr.replace("X","1",1)]

                for addr in done:
                    mem["".join(addr)] = int(line[2])
    return sum(mem.values())

print(part1())
print(part2())
