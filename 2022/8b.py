from functools import reduce


with open("inputs/day8.txt") as f:
    s = f.read()

# s="""30373
# 25512
# 65332
# 33549
# 35390"""

def look(trees, row, col)->bool:
    score = 0
    above = 0
    for r in trees[:row][::-1]:
        above += 1
        if r[col] >= trees[row][col]: break
    
    below = 0
    for r in trees[row+1:]:
        below += 1
        if r[col] >= trees[row][col]: break
    
    right = 0
    for c in range(col+1, len(trees[row])):
        right += 1
        if trees[row][c] >= trees[row][col]: break

    left = 0
    for c in range(col):
        left += 1 
        if trees[row][col-c-1] >= trees[row][col]: break

    
    return above*below*left*right

    # above= reduce((lambda x, y: x * y), above)
    # below= reduce((lambda x, y: x * y), below)
    # left= reduce((lambda x, y: x * y), left)
    # right= reduce((lambda x, y: x * y), right)

s = list(map(list, s.split("\n")))
for row in range(len(s)):
    s[row] = list(map(int, s[row]))

trees  = []
for row in range(1, len(s)-1):
    for col in range(1, len(s[row])-1):
        # print(row, col, look(s, row, col))
        trees.append(look(s, row, col))
        
print(max(trees))



