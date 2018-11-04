import numpy as np
# from flask import Flask
# app = Flask(__name__)


class Game():

    def __init__(self,user,comp):
        self.board = np.zeros((3,3))
        self.turns = 0
        self.comp = comp
        self.user = user

    def update_game(self,board,turns):
        self.board = board
        self.turns = turns

    def get_comp_move(self):
        return move
    
    ## Might not need
    def update_board(self, val, index):
        row = (val-1) // 3
        col = (val-1) % 3
        if self.board[row,col] == 0:
            self.board[row,col] = val
            self.turns += 1
            return True
        else:
            return False

    ## probably don't need
    def check_winner(self):
        for row in self.board:
            if np.all(row == self.comp):
                return True, 'computer'
            elif np.all(row == self.user):
                return True, 'user'
        for i in range(len(3)):
            col = self.board[:,i]
            if np.all(col == self.comp):
                return True, 'computer'
            elif np.all(col == self.user):
                return True, 'player'
        diag1 = [self.board[0,0], self.board[1,1], self.board[2,2]]
        diag2 = [self.board[0,2], self.board[1,1], self.board[2,0]]
        if np.all(diag1 == self.comp) or np.all(diag2 == self.comp):
            return True, 'computer'
        elif np.all(diag1 == self.user) or np.all(diag2 == self.user):
            return True, 'player'
        return False
    
    def check_draw(self):
        if self.turns == 9:
            return True

    def get_comp_move(self):
        return

