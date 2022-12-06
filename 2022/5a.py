import re

with open("inputs/day5.txt") as f:
    s = f.read()

# s = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

layout = s.split("\n\n")[0]
instructions = s.split("\n\n")[1]

creates = [[] for _ in range(1, len(layout.split("\n")[0]),4)]
for line in s.split("\n\n")[0].split("\n")[:-1]:
    for i, letter in enumerate(range(1, len(line),4)):
        if line[letter]!=" ":
            creates[i].append(line[letter])
creates = [list(reversed(x)) for x in creates]

for inst in instructions.split("\n"):
    i = inst.split(" ")
    N, a, b = map(int, (i[1], i[3], i[5]))
    for n in range(N):
        creates[b-1].append(creates[a-1].pop())
print("".join([stack.pop() for stack in creates]))

