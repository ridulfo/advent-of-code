with open("inputs/day9.txt") as f:
    s = f.read()
# s = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

def t_step(H, T):
    if abs(H[0]-T[0])>1 and abs(H[1]-T[1])>1:
        print("Too far")
        return False


h_history = []
t_history = set()
H = (0,0)
T = (0,0)
h_history.append(H)

for inst in s.split("\n"):
    direction, steps = inst.split(" ")[0], int(inst.split(" ")[1])
    print("-"*10, inst, "-"*10)
    for step in range(steps):
        if direction == "R":
            H = (H[0]+1, H[1])
        elif direction == "L":
            H = (H[0]-1, H[1])
        elif direction == "U":
            H = (H[0], H[1]+1)
        elif direction == "D":
            H = (H[0], H[1]-1)
        

        if abs(H[0]-T[0])>0 and abs(H[1]-T[1])>0 and (abs(H[0]-T[0])>1 or abs(H[1]-T[1])>1):
            print("D")
            d = 1 if H[0]>T[0] else -1
            T=(T[0] + d, T[1])
            d = 1 if H[1]>T[1] else -1
            T=(T[0], T[1] +d)
        elif abs(H[0]-T[0])>1:
            print("H")
            d = 1 if H[0]>T[0] else -1
            T=(T[0] + d, T[1])
        elif abs(H[1]-T[1])>1:
            print("V")
            d = 1 if H[1]>T[1] else -1
            T=(T[0], T[1] +d)

        # # not touching
        # while abs(H[0]-T[0])>1 or abs(H[1]-T[1])>1:
        #     T = h_history.pop(0)

        # h_history.append(H)
        t_history.add(T)
        print(H, T)
print(len(t_history))

