with open("inputs/day4.txt") as f:
    assignments = f.read()

count = 0
for assignment in assignments.split("\n"):
    as1, as2 = assignment.split(",")
    as1 = list(map(int, as1.split("-")))
    as2 = list(map(int, as2.split("-")))

    if as1[0] <= as2[0] <= as2[1] <= as1[1]:
        count += 1
    elif as2[0] <= as1[0] <= as1[1] <= as2[1]:
        count += 1
print(count)

