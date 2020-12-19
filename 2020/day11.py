import itertools

def getseats():
    with open("input11.txt", "r") as f:
        return [[c for c in line] for line in f.read().strip().split("\n")]

def printer(seats):
    for row in seats:
        print("".join(row))
    print()

def part1():
    initialseats = [["#" if c=="L" else "." for c in line] for line in getseats()]
    surrCoord = list(itertools.product((-1,0,1), (-1,0,1)))
    surrCoord.remove((0,0))
    def iterate(seats):
        totchange = 0
        nextSeats = [["X" for _ in range(len(seats[0]))] for _ in range(len(seats))]
        for row in range(len(seats)):
            for seat in range(len(seats[row])):
                spot = seats[row][seat]
                nextSeats[row][seat] = spot
                if spot in "#L":
                    surrounding = 0
                    for r,s in surrCoord:
                        if 0<=row+r<len(seats) and 0<=seat+s<len(seats[row]) and seats[row+r][seat+s]=="#":
                            surrounding+=1
                    if spot=="L" and surrounding==0:
                        nextSeats[row][seat] = "#"
                        totchange+=1
                    elif spot=="#" and surrounding >= 4:
                        nextSeats[row][seat] = "L"
                        totchange+=1
        return totchange, nextSeats

    totchange, nextSeats = iterate(initialseats)
    while True:
        totchange, nextSeats = iterate(nextSeats)
        if totchange==0: break
    return sum([1 for seat in sum(nextSeats, list()) if seat=="#"])

def part2():
    initialseats = [["#" if c=="L" else "." for c in line] for line in getseats()]
    direcs = list(itertools.product((-1,0,1), (-1,0,1))) #(y,x)
    direcs.remove((0,0))
    def countInDirection(direc, seats, seat):
        y, x = seat
        y += direc[0] # y coor
        x += direc[1] # x coor
        while 0<=y<len(seats) and 0<=x<len(seats[0]):
            if seats[y][x] in "#":
                return 1
            if seats[y][x] in "L":
                return 0
            y += direc[0]
            x += direc[1]
        return 0

    def iterate(seats):
        totchange = 0
        nextSeats = [["X" for _ in range(len(seats[0]))] for _ in range(len(seats))]
        for y in range(len(seats)):
            for x in range(len(seats[0])):
                spot = seats[y][x]
                nextSeats[y][x] = spot
                if spot in "L#":
                    surrounding = 0
                    for direc in direcs:
                        surrounding+=countInDirection(direc, seats, (y, x))
                    if spot=="L" and surrounding==0:
                        nextSeats[y][x] = "#"
                        totchange+=1
                    elif spot=="#" and surrounding >= 5:
                        nextSeats[y][x] = "L"
                        totchange+=1
        return totchange, nextSeats

    totchange, nextSeats = iterate(initialseats)
    while True:
        totchange, nextSeats = iterate(nextSeats)
        if totchange==0: break
    return sum([1 for seat in sum(nextSeats, list()) if seat=="#"])


from time import time
def timeit(func):
    t0 = time()
    result = func()
    t1 = time()
    print("Answer:", result, "Time:", round((t1-t0)*1000, 2), "ms")
#timeit(part1)
timeit(part2)
