ex = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

m = [list(map(int, (list(x)))) for x in ex.split('\n')]
openList = []
closedList = set()
g, h, f = {}, {}, {}
start = (0, 0)
g[start]=0
f[start]=0
openList.append(start)
while len(openList) > 0:
    openList.sort(key=lambda x: f[x])
    curr = openList.pop(0)
    print(curr, g[curr])
    closedList.add(curr)
    if curr == (len(m), len(m[0])):
        print("Winnner", curr)
        print(g[curr])
        break
    adj = [(curr[0]-1, curr[1]), (curr[0]+1, curr[1]),
           (curr[0], curr[1]-1), (curr[0], curr[1]+1)]
    for child in adj:
        if child[0] < 0 or child[1] < 0 or child[0] >= len(m) or child[1] >= len(m[0]):
            continue
        if child in closedList:
            continue
        g[child] = g[curr] + m[child[0]][child[1]]
        h[child] = abs(child[0] - len(m)) + abs(child[1] - len(m[0]))
        f[child] = g[child] + h[child]
        if child in openList and g[child] > g[sorted(openList)[0]]:
            continue
        openList.append(child)
