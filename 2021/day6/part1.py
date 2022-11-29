import sys
ages = list(map(int, sys.stdin.read().split(",")))
for n in range(80):
    for i in range(len(ages)):
        ages[i]-=1
        if ages[i] < 0:
            ages[i] = 6
            ages.append(8)

print(len(ages))