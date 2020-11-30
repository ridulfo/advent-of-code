from time import sleep


def countorbits(orbitstext):
    orbits = dict()
    for line in orbitstext.split("\n"):
        if line=="": continue
        parent, child = line.split(")")
        if parent not in orbits:
            orbits[parent] = list()
        orbits[parent].append(child)

    for k, w in orbits.items():
        print(k, w)

    def recursive(key, c):
        c+=1
        print(key, c)
        sleep(0.5)
        if key not in orbits:
            return c

        for orbit in orbits[key]:
            c=recursive(orbit, c)

        return c

    count = sum([recursive(x, 0) for x in orbits.keys()])
    return count


testData = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

print(countorbits(testData))
