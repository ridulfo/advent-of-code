with open("inputs/day6.txt") as f:
    s = f.read()

for n in range(len(s)-4):
    if len(set(s[n:n+4]))==4:
        print(n+4)
        break
