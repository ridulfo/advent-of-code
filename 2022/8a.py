with open("inputs/day8.txt") as f:
    s = f.read()

# s="""30373
# 25512
# 65332
# 33549
# 35390"""

def look(trees, row, col)->bool:
    """Function returns if the tree is visible from the current position"""
    above = [r[col] for r in trees[:row]]
    if max(above) < trees[row][col]:
        return True
    below = [r[col] for r in trees[row+1:]]
    if max(below) < trees[row][col]:
        return True
    left = [trees[row][c] for c in range(col)]
    if max(left) < trees[row][col]:
        return True
    right = [trees[row][c] for c in range(col+1, len(trees[row]))]
    if max(right) < trees[row][col]:
        return True
    return False

s = list(map(list, s.split("\n")))
for row in range(len(s)):
    s[row] = list(map(int, s[row]))

c = 0
for row in range(1, len(s)-1):
    for col in range(1, len(s[row])-1):
        if look(s, row, col):
            c += 1
        
print(c+2*len(s)+2*len(s[0])-4)



