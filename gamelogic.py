import numpy as np




class game():

    def __init__(self):
        self.board = np.zeros((3,3))
        self.turns = 0
    
    def update_board(self, val, index):
        row = (val-1) // 3
        col = (val-1) % 3
        if self.board[row,col] == 0:
            self.board[row,col] = val
            self.turns += 1
            return True
        else:
            return False

    def check_winner(self):
        for row in self.board:
            if np.all(row == 1):
                return True, 'computer'
            elif np.all(row == 2):
                return True, 'player'
        for i in range(len(3)):
            col = self.board[:,i]
            if np.all(col == 1):
                return True, 'computer'
            elif np.all(col == 2):
                return True, 'player'
        diag1 = [self.board[0,0], self.board[1,1], self.board[2,2]]
        diag2 = [self.board[0,2], self.board[1,1], self.board[2,0]]
        if np.all(diag1 == 1) or np.all(diag2 == 1):
            return True, 'computer'
        elif np.all(diag1 == 2) or np.all(diag2 == 2):
            return True, 'player'
        return False
    
    def check_draw(self):
        if self.turns == 9:
            return True

    def get_comp_move(self):
        return

