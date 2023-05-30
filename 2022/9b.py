with open("inputs/day9.txt") as f:
    s = f.read()
# s = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""

h_history = []
t_history = set()
H = {"x":0, "y":0}
Ts = [{"x":0, "y":0} for _ in range(1, 10)]

for inst in s.split("\n"):
    direction, steps = inst.split(" ")[0], int(inst.split(" ")[1])
    print("-"*10, inst, "-"*10)
    for step in range(steps):
        if direction == "R":
            H["x"] += 1
        elif direction == "L":
            H["x"] -= 1
        elif direction == "U":
            H["y"] += 1
        elif direction == "D":
            H["y"] -= 1
        

        for i in range(len(Ts)):
            T = Ts[i]
            head = H if i==0 else Ts[i-1]
            if abs(head["x"]-T["x"])>0 and abs(head["y"]-T["y"])>0 and (abs(head["x"]-T["x"])>1 or abs(head["y"]-T["y"])>1):
                T["x"]+= 1 if head["x"]>T["x"] else -1
                T["y"]+=1 if head["y"]>T["y"] else -1
            elif abs(head["x"]-T["x"])>1:
                T["x"] += 1 if head["x"]>T["x"] else -1
            elif abs(head["y"]-T["y"])>1:
                T["y"] += 1 if head["y"]>T["y"] else -1

        t_history.add(str(Ts[-1]))
        print(H, T, i)
print(len(t_history))

