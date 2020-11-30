wirePaths = open("inputDay3.txt","r").read().split("\n")
wire1 = wirePaths[0].split(",")
wire2 = wirePaths[1].split(",")
#wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
#wire2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

def coordinatesPassed(directions):
	coordinates = {}
	current = (0,0)
	length = 0
	coordinates[current] = length
	for direction in directions:
		d = direction[0]
		dist = int(direction[1:])
		DX = (-1 if d == "L" else 1) if d in "RL" else 0
		DY = (-1 if d == "D" else 1) if d in "UD" else 0
		for _ in range(dist):
			length += 1
			current = (current[0] + DX, current[1] + DY)
			if current not in coordinates:
				coordinates[current] = length
	return coordinates

#Part 1
coordinates1 = coordinatesPassed(wire1)
coordinates2 = coordinatesPassed(wire2) 
equal = []
for cor1 in coordinates1.keys():
	if cor1 in coordinates2.keys():
		equal.append(abs(cor1[0])+abs(cor1[1]))
equal.sort()
equal.remove(0)
print(min(equal))

#Part 2
coordinates1 = coordinatesPassed(wire1)
coordinates2 = coordinatesPassed(wire2) 
equal = []
for cor1 in coordinates1.keys():
	if cor1 in coordinates2.keys():
		equal.append(coordinates1[cor1] + coordinates2[cor1])
equal.sort()
equal.remove(0)
print(min(equal))