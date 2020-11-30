
import time
import re
#372304-847060


def part1(x): #Returns if the number matches the criterium for part 1
	l = list(str(x)) #Is it increasing
	for n in range(1,len(l)):
		if l[n-1]>l[n]:
			return False

	foundDouble = False #Does it contain at least one double
	l = list(str(x))
	for n in range(1,len(l)):
		if l[n-1]==l[n]:
			foundDouble = True
	return foundDouble

def part2(x):
	resultPart1 = part1(x)
	if not resultPart1==True:
		return resultPart1
	l = re.findall(r"(\w)\1+", str(x))
	multipleIsLessThanThree = False
	for c in l:
		if str(x).count(c)<3:
			multipleIsLessThanThree=True
	return multipleIsLessThanThree

#Part 1
start = time.time()
count = 0
for n in range(372304,847060):
	if part1(n):
		count+=1
print(time.time()-start)
print(count)
#Part 2
start = time.time()
count = 0
for n in range(372304,847060):
	if part2(n):
		count+=1
print(time.time()-start)
print(count)