import re
from functools import reduce

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


class Bingo:
    def __init__(self, board):
        self.board = board
        self.board_marked = [[0 for _ in range(5)] for _ in range(5)]
        self.solved = False        
        self.score = reduce(lambda a,b:a+b,[reduce(lambda a,b:a+b, row) for row in self.board])

    def is_solved(self):
        for i in range(5):
            if reduce(lambda a,b:a+b, self.board_marked[i]) == 5:
                return True
            elif reduce(lambda a,b:a+b, [row[i] for row in self.board_marked]) == 5:
                return True
        return False

    def draw(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.board_marked[i][j] = 1
                    self.board[i][j] = 0

        self.solved = self.is_solved()
        self.score = reduce(lambda a,b:a+b,[reduce(lambda a,b:a+b, row) for row in self.board])


bingo_games = [Bingo(board) for board in boards]

for draw in draw_list:
    if len(bingo_games) == 0:
        break
    elif len(bingo_games) == 1:
        bingo_games[0].draw(draw)
        if bingo_games[0].solved:
            print(bingo_games[0].score * draw)
            bingo_games = []
    else:
        for bingo in bingo_games:
            bingo.draw(draw)
        bingo_games = [bingo for bingo in bingo_games if bingo.solved==False]