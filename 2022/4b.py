with open("inputs/day4.txt") as f:
    assignments = f.read()

count = 0
for line in assignments.split("\n"):
    as1, as2 = line.split(",")
    a1,a2 = list(map(int, as1.split("-")))
    b1,b2 = list(map(int, as2.split("-")))
    if a1 <= b1 <= b2 <= a1:
        count += 1
    elif b1 <= a1 <= a2 <= b2:
        count += 1
    elif a1<=b1<=a2 or a1<=b2<=a2:
        count+=1
    elif b1<=a1<=b2 or b1<=a2<=b2:
        count+=1

print(count)