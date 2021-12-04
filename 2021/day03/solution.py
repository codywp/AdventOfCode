import numpy as np

class BingoBoard:
    def __init__(self, board):
        self.board = np.array([[int(i) for i in line.split()] for line in board.strip().split('\n')])
        self.pulled = np.zeros((5,5))
        self.locations = dict()
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.locations |= {self.board[i][j]: (i, j)}
        self.another = True
    
    def is_loser(self): return self.another

    def check_board(self):
        columns = np.sum(self.pulled, axis=0)
        rows = np.sum(self.pulled, axis=1)
        return columns, rows

    def get_winning_sum(self):
        self.another = False
        return np.sum(self.board[np.where(self.pulled == 0)])

    def new_number(self, value):
        if value in self.locations: self.pulled[self.locations[value]] = 1
        columns, rows = self.check_board()
        return 5 in columns or 5 in rows

def solve1(bingoBoards, pulled_nums):
    winners = []
    for num in pulled_nums:
        for board in bingoBoards:
            if board.new_number(num):
                winners.append(board.get_winning_sum() * num)
        bingoBoards = list(filter(lambda board: board.is_loser(), bingoBoards))
    print(winners[0], winners[-1])

pulled_nums, *boards = open('input.txt').read().split('\n\n')
pulled_nums = [int(i) for i in pulled_nums.split(',')]
boards = [BingoBoard(board) for board in boards]
solve1(boards, pulled_nums)
