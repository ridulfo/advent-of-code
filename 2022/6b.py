with open("inputs/day6.txt") as f:
    s = f.read()

for n in range(len(s)-14):
    if len(set(s[n:n+14]))==14:
        print(n+14)
        break
