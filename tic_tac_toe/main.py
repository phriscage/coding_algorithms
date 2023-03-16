#!/usr/bin/env python3
"""
    TicTacToe game logic example
"""
import sys
import uuid
import datetime

class TicTacToe(object):
    """ main class """

    def __init__(self, player1, player2):
        """ instantiate the class """
        self.game_board = self.create_game()
        self.player1 = player1
        self.player2 = player2
        self.game_id = str(uuid.uuid4())
        self.history = list()

    def _current_time(self):
        """ get the current time in ISO 8601 format """
        return datetime.datetime.now().isoformat()

    def _is_position_set(self, row, col):
        """ return true if position set """
        try:
            if not self.game_board[row][col] == 0:
                return True
        except IndexError as error:
            return True
        return False

    def _is_winner(self):
        """ check if there is a winner """
        winner_type = "horizontal"
        for idx, row in enumerate(self.game_board):
            uniq_row = set(row)
            if len(uniq_row) == 1 and any(uniq_row):
                print("%s row #%d is a winner" % (winner_type, idx))
                return True
        winner_type = "vertical"
        for y in range(len(self.game_board)):
            if self.game_board[0][y] != 0:
                if self.game_board[0][y] == self.game_board[1][y] == self.game_board[2][y]:
                    print("%s col #%d is a winner" % (winner_type, y))
                    return True
        winner_type = "diagonal"
        if self.game_board[1][1] != 0:
            if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2]:
                print("%s row left is a winner" % winner_type)
                return True
            if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0]:
                print("%s row righ is a winner" % winner_type)
                return True
        return False

    def create_game(self):
        return [[0 for x in range(3)] for y in range(3)]

    def get_game(self):
        """ display the game board """
        print("-" * 14)
        print("#   0   1   2")
        for idx, row in enumerate(self.game_board):
            print("%d   %s" % (idx, row))

    def update_position(self, row, col, value, player):
        """ set the position for the player """
        if self._is_position_set(row, col):
            raise TypeError("%d, %d is already set or out of range" % (row, col))
        self.game_board[row][col] = value
        self.history.append({
            'game_id': self.game_id,
            'player': player,
            'action': 'update',
            'row': row,
            'col': col,
            'value': value,
            'created_at': self._current_time()
            })
        self._is_winner()

    def run(self, **args):
        """ run through the game """
        while not self._is_winner():
            try:
                name = input("What is the your name: %s, %s?\n" % (self.player1, self.player2))
                value = 1
                if name == self.player2:
                    value = 2
                left = int(input("What is the left position?\n"))
                right = int(input("What is the right position?\n"))
                self.update_position(left, right, value, name)
                self.get_game()
            except Exception as error:
                print("Try again: %s", error)


if __name__ == '__main__':
    player1 = "abc"
    player2 = "xyz"
    data = {
            'player1': "abc",
            'player2': "xyz"
            }
    game = TicTacToe(*data)
    game.run()
    ## failures
    #game.update_position(1,1,1,player1)
    #game.update_position(3,3,1,player1)
    ## hori winner
    #game.update_position(0,2,1,player1)
    #game.update_position(2,1,2,player2)
    ## vert winner
    print(game.history)
