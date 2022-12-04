with open("inputs/day2.txt") as f:
    s = f.read()
print(sum([[3,0,6][(ord(line[0])-ord("A")-(ord(line[2])-ord("X")))%3]+ord(line[2])-ord("X")+1 for line in s.split("\n")]))