f = open("input.txt", "r")
modules = f.read().split("\n")
f.close()
fuelEq = lambda x: int(x)//3-2

#Part 2
def fuel4fuel(fuel):
	if fuel<1:
		return 0
	else:
		return fuel+fuel4fuel(fuelEq(fuel))

modulesFuel = list(map(lambda x: fuel4fuel(fuelEq(int(x))),modules))
print(sum(modulesFuel))

#Part 1
modulesFuel = list(map(fuelEq,modules))
print(sum(modulesFuel))
