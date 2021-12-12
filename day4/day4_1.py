import re

# open inputs
with open("day4_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

# make draw list
draw_list = [int(i) for i in inputs[0].split(',')]

# make bingo board list
board_input = [re.findall(r'\d+',item) for item in inputs[2:]]
boards = []
temp_board = []
for li in board_input:
    if li:
        temp_board.append([int(i) for i in li])
    if len(temp_board) == 5:
        boards.append(temp_board)
        temp_board = []

# determine a board is solved or not, if solved return score
def bingo_win(board, draws):
    drawed_idx = [[0 for _ in range(5)] for _ in range(5)]
    for draw in draws:
        for row in board:
            if draw in row:
                i, j = board.index(row), row.index(draw)
                drawed_idx[i][j] = 1
    row_sums = [sum(row) for row in drawed_idx]
    col_sums = [0 for _ in range(5)]
    for i in range(5):
        for row in drawed_idx:
            col_sums[i] += row[i]

    if max(row_sums) == 5 or max(col_sums) == 5:
        remaining_sum = 0
        for row in drawed_idx:
            for j in range(5):
                if row[j] == 0:
                    remaining_sum += board[drawed_idx.index(row)][j]
        score = remaining_sum * draws[-1]
        return True, score

    return False, None

# find winning board's score
draws = []
found = False
for draw in draw_list:    
    draws.append(draw)
    for board in boards:
        if bingo_win(board, draws)[0]:
            print(bingo_win(board, draws))
            found = True
    if found:
        break
