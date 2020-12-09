def getSeats():
    with open("inputDay5.txt", "r") as f:
        return [(row[:7], row[7:]) for row in f.read().strip().split("\n")]

def part1():
    siteids = list()
    for row, col in getSeats():
        pos = (0, 127)
        for let in row:
            if let=="F": pos = (pos[0], (pos[0] + pos[1])//2)
            else:        pos = ((pos[0] + pos[1])//2+1, pos[1])
        assert pos[0]==pos[1]
        row = pos[0]

        pos = (0, 7)
        for let in col:
            if let=="L": pos = (pos[0], (pos[0] + pos[1])//2)
            else:        pos = ((pos[0] + pos[1])//2+1, pos[1])
        assert pos[0]==pos[1]
        col = pos[0]
        siteids.append(row*8+col)

    return max(siteids)

def part2():
    seats = list()
    for row, col in getSeats():
        pos = (0, 127)
        for let in row:
            if let=="F": pos = (pos[0], (pos[0] + pos[1])//2)
            else:        pos = ((pos[0] + pos[1])//2+1, pos[1])
        assert pos[0]==pos[1]
        row = pos[0]

        pos = (0, 7)
        for let in col:
            if let=="L": pos = (pos[0], (pos[0] + pos[1])//2)
            else:        pos = ((pos[0] + pos[1])//2+1, pos[1])
        assert pos[0]==pos[1]
        col = pos[0]
        seats.append((row, col))

    seats.sort()
    expcseat = seats[0]
    seatIter = iter(seats)
    for seat in seatIter:
        if seat!=expcseat:
            break
        expcseat = (seat[0]+(1 if seat[1]==7 else 0), (seat[1] + 1)%8)
    return expcseat [0]*8+expcseat[1]

print(part1())
print(part2())
