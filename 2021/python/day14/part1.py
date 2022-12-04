import sys
from collections import Counter

ex = sys.stdin.read()
ex = ex.split("\n")
temp = ex[0]
pairs = dict([l.split(" -> ") for l in ex[2:]])
for iter in range(10):
    next_temp = ""
    for i in range(len(temp)-1):
        pair = temp[i:i+2]
        next_temp += pair[0] + pairs[pair]
        if i==len(temp)-2:
            next_temp += pair[1]
    temp = next_temp
    freq = Counter(temp)
    most = max(freq.values())
    least = min(freq.values())
    print(iter, most-least)
