import sys
ages = dict(zip(range(0, 9), [0]*9))
for age in map(int, sys.stdin.read().split(",")):
    ages[age]+=1

for n in range(256):
    next_ages = dict(zip(range(0, 9), [0]*9))
    for age in ages.keys():
        if age==0: 
            next_ages[8] += ages[age]
            next_ages[6] += ages[age]
        else:
            next_ages[age-1] += ages[age]
    ages = next_ages
print(sum(ages.values()))