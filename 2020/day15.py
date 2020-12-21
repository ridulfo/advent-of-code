def getNums():
    #starting = [3,1,2]
    starting = [1,17,0,10,18,11,6]
    return starting

def part1():
    mem = dict()
    for i, num in enumerate(getNums()[:-1], start=1):
        mem[num] = i
    turn = len(getNums())
    last = getNums()[-1]
    next = None
    while turn<2020: #Every iteration of the loop we determine the next number
        if last not in mem:
            next = 0
        else:
            next = turn - mem[last]
        turn+=1
        mem[last] = turn-1
        last = next
    return next

def part2():
    mem = dict()
    for i, num in enumerate(getNums()[:-1], start=1):
        mem[num] = i
    turn = len(getNums())
    last = getNums()[-1]
    next = None
    while turn<30000000: #Every iteration of the loop we determine the next number
        if last not in mem:
            next = 0
        else:
            next = turn - mem[last]
        turn+=1
        mem[last] = turn-1
        last = next
    return next



print(part1())
print(part2())
