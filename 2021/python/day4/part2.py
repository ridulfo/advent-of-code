import sys
ex = sys.stdin.read()

nums = list(map(int, ex.split("\n")[0].split(',')))
boards = []
for board in ex.split('\n\n')[1:]:
    columns, rows = [], []
    for row in board.split("\n"):
        rows.append(list(map(int, row.split())))  # Horizontal
    for col in range(5):
        columns.append([rows[row][col] for row in range(5)])
    boards.append(columns+rows)

boards_set = [list(map(set,b)) for b in boards]
score = lambda b: sum(set.union(*b))

for num in map(int, nums):
    for board in boards_set:
        for row in board:
            if num in row: row.remove(num)
    boards_set = [board for board in boards_set if all(len(row) > 0 for row in board)]
    if len(boards_set) == 0:
        break
print(score(board)*num)