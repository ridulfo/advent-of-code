with open("inputs/day10.txt") as f:
    s = f.read()

x = 1
cycle = [1] 
for line in s.split("\n"):
    if line.startswith("addx"):
        cycle.append(x)
        cycle.append(x)
        x += int(line.split(" ")[1])
    elif line.startswith("noop"):
        cycle.append(x)
for i, v  in enumerate(cycle):
    print(i+1, v)


print(sum([n*cycle[n] for n in range(20, 221, 40)]))