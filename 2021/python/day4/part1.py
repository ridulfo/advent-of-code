import sys
ex = sys.stdin.read()

nums = ex.split("\n")[0].split(',')
boards = []
for board in ex.split('\n\n')[1:]:
    columns, rows = [], []
    for row in board.split("\n"):
        rows.append(list(map(int,row.split()))) # Horizontal
    for col in range(5):
        columns.append([rows[row][col] for row in range(5)])
    boards.append(columns+rows)

set_boards = [list(map(set,b)) for b in boards]

for num in map(int, nums):
    for i, board in enumerate(set_boards):
        for row in board:
            if num in row:
                row.remove(num)
        if any(len(row) == 0 for row in board):
            print(sum(set.union(*board))*num)
            exit()