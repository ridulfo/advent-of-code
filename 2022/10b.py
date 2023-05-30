with open("inputs/day10.txt") as f:
    s = f.read()

x = 1
cycles = [1] 
for line in s.split("\n"):
    if line.startswith("addx"):
        cycles.append(x)
        cycles.append(x)
        x += int(line.split(" ")[1])
    elif line.startswith("noop"):
        cycles.append(x)

sprite = 0 # (0, 1, 2)
img = " " # 40 wide, 6 tall
for i, cycle in enumerate(cycles):
    sprite = cycle
    x = i % 40
    if x == 0:
        img += "\n"
    if x in (sprite, sprite+1, sprite+2):
        img += "#"
    else:
        img += " "
print(img)