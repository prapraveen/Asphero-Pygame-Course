import random

class StartingBoards:
    def __init__(self):
        self.boards = [['1','2','3',  '4','5','6',  '7','8','9'],
            ['4','5','6',  '7','8','9',  '1','2','3'],
            ['7','8','9',  '1','2','3',  '4','5','6'],

            ['2','3','1',  '5','6','4',  '8','9','7'],
            ['5','6','4',  '8','9','7',  '2','3','1'],
            ['8','9','7',  '2','3','1',  '5','6','4'],

            ['3','1','2',  '6','4','5',  '9','7','8'],
            ['6','4','5',  '9','7','8',  '3','1','2'],
            ['9','7','8',  '3','1','2',  '6','4','5']]
        
    def generate_starting_board(self):
        for i in range(75):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            board = self.boards
            board[row][col] = '_'
        return board
