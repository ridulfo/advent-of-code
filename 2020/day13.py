from functools import reduce
import math
from time import time
def getNotes():
    with open("input13.txt", "r") as f:
        text = f.read().strip().split("\n")
        return (int(text[0]), [t for t in text[1].split(",")])

def part1():
    start, ids = getNotes()
    ids = [int(t) for t in ids if t!="x"]
    for t in range(start, start+max(ids)+1):
        for id in ids:
            if t%id==0: return (t-start)*id

def part2():
    _, ids = getNotes()
    ranges = [range(-i,10**20,int(id)) for i, id in enumerate(ids) if id!="x"]
    ranges.sort(key=lambda x: x.step, reverse=True)
    lastmag, lasttime = 0, time()
    for n in ranges[0]:
        found = True
        for r in ranges[1:]:
            if n not in r:
                found=False
                break
        if found:
            return n
        #if n>0 and int(math.log(n,10))>lastmag:
        #    lastmag = int(math.log(n,10))
        #    print(n, time()-lasttime)
        #    lasttime = time()

def part2b():
    #Chinese remainder code from rosetta
    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod
     
     
     
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1
     
    _, ids = getNotes()

    a, n= zip(*[(-i,int(id)) for i, id in enumerate(ids) if id!="x"])
    a,n = list(a),list(n)
    a[0] = -n[0]
    return chinese_remainder(n,a) 

print(part1())
#print(part2())
print(part2b())
