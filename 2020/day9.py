from itertools import combinations
def getNum():
    with open("input9.txt", "r") as f:
        return [int(x) for x in f.read().strip().split("\n")]

def part1():
    nums = getNum()
    pre = 25
    for i, n in enumerate(nums[25:], 25):
        if n not in [sum(pair) for pair in combinations(nums[i-25:i], 2)]:
            return n

    return getNum()

def part2():
    num = part1()
    nums = getNum()
    for n in range(len(nums)):
        s = m = 0 
        while s<num and n+m<len(nums):
            s += nums[n+m]
            m+=1
        if s==num:
            l = nums[n:n+m]
            return min(l)+max(l) 

print(part1())
print(part2())
