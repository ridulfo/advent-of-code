from math import cos, sin, radians
def getActions():
    with open("input12.txt", "r") as f:
        return [(line[0], int(line[1:])) for line in f.read().strip().split("\n")]

def part1():
    actions = getActions()
    x=y=direc=0
    for op, arg in actions:
        if op=="N": y+=arg
        elif op=="S": y-=arg
        elif op=="E": x+=arg
        elif op=="W": x-=arg
        elif op=="L": direc+=arg
        elif op=="R": direc-=arg
        elif op=="F":
            y+=arg*sin(radians(direc))
            x+=arg*cos(radians(direc))
    return round(abs(x)+abs(y))


def part2():
    actions = getActions()
    x=y=0
    wx,wy=10,1
    for op, arg in actions:
        if op=="N": wy+=arg
        elif op=="S": wy-=arg
        elif op=="E": wx+=arg
        elif op=="W": wx-=arg
        elif op in "RL":
            arg = radians(arg)
            if op=="R": arg *= -1
            wx, wy = cos(arg)*wx - sin(arg)*wy, sin(arg)*wx + cos(arg)*wy
        elif op=="F":
            x+=wx*arg
            y+=wy*arg
    return round(abs(x)+abs(y))



print(part1())
print(part2())
