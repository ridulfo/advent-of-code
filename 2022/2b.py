with open("inputs/day2.txt") as f:
    s = f.read()
# Convert from instruction to game
s = "\n".join([line[0:2] + chr((ord(line[0])-ord("A")+[-1, 0, 1][ord(line[2])-ord("X")])%3+ord("X")) for line in s.split("\n")])
# Same as 2a.py
print(sum([[3,0,6][(ord(line[0])-ord("A")-(ord(line[2])-ord("X")))%3]+ord(line[2])-ord("X")+1 for line in s.split("\n")]))