import sys
from collections import Counter

ex = sys.stdin.read()
ex = ex.split("\n")
temp = ex[0]
temp = [temp[i:i+2] for i in range(len(temp)-1)]
temp_dict = Counter(temp)
pairs = dict([l.split(" -> ") for l in ex[2:]])
for iter in range(40):
    next_temp_dict = dict()
    for pair, count in temp_dict.items():
        pair1, pair2 = pair[0]+pairs[pair], pairs[pair]+pair[1]
        if pair1 not in next_temp_dict:
            next_temp_dict[pair1] = count
        else:
            next_temp_dict[pair1] += count
    
        if pair2 not in next_temp_dict:
            next_temp_dict[pair2] = count
        else:
            next_temp_dict[pair2] += count
    temp_dict = next_temp_dict

    unique = set("".join(temp_dict))
    c1 = dict(zip(unique, [0]*len(unique)))
    c2 = dict(zip(unique, [0]*len(unique)))
    for pair, count in temp_dict.items():
        c1[pair[0]] += count
        c2[pair[1]] += count
    c3 = dict()
    for key in c1:
        c3[key] = max(c1[key], c2[key])
print(max(c3.values())-min(c3.values()))