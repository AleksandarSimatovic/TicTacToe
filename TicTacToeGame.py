from math import *


class TicTacToeGame:
    def __init__(self, sign_p1="X", sign_p2="0", sign_at_start="-", starting_player=1):
        self.size = 3
        self.board = []
        for pos in range(self.size):
            row = []
            for column in range(self.size):
                row.append(sign_at_start)
            self.board.append(row)
        self.sign_p1 = sign_p1
        self.sign_p2 = sign_p2
        self.sign_at_start = sign_at_start
        self.starting_player = starting_player
        self.player_turn = starting_player
        self.turns_used = 0
        self.game_ended = False

    def print_board(self):
        for row_num in range(self.size):
            for col_size in range(self.size):
                print(self.board[row_num][col_size], end=" ")
            print("\n")

    def get_player_sign(self):
        if self.player_turn == 1:
            return self.sign_p1
        else:
            return self.sign_p2

    def change_player(self):
        if self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1

    def check_winning_conditions(self, x2, y2):
        for x in range(self.size):
            for y in range(self.size):
                if x == x2 and y == y2:
                    if self.board[x][y] != self.sign_at_start:
                        if self.board[0][y] == self.board[1][y] and self.board[0][y] == self.board[2][y]:
                            return self.find_winner(x, y)
                        if self.board[x][0] == self.board[x][1] and self.board[x][0] == self.board[x][2]:
                            return self.find_winner(x, y)
                        if x == y:
                            if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
                                return self.find_winner(x, y)
                        if x + y == self.size - 1:
                            if self.board[0][0] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
                                return self.find_winner(x, y)
                        return 0

    def find_winner(self, x, y):
        if self.board[x][y] == self.sign_p1:
            return "Game ended, player 1 wins!"
        else:
            return "Game ended, player 2 wins!"

    def play_game_text(self):
        while not self.game_ended:
            try:
                highest_value = self.size*self.size
                self.print_board()
                print("Player to move: " + str(self.player_turn))
                answer = input("Choose a spot (1-" + str(highest_value) + "): ")
                if answer == "0":
                    raise IndexError
                self.make_move_text(int(answer))
            except TypeError as err:
                print(err)
            except IndexError as err:
                print(err)
            except ValueError as err:
                print(err)

    def make_move_text(self, position):
        if not self.game_ended:
            x = floor((position - 1) / self.size)
            y = (position - 1) % self.size
            if self.board[x][y] == self.sign_at_start:
                self.board[x][y] = self.get_player_sign()
                self.turns_used += 1
                result = self.check_winning_conditions(x, y)
                if result != 0:
                    print(result)
                    self.print_board()
                    self.game_ended = True
                elif self.turns_used == self.size*self.size:
                    print("Game ended, its a draw!")
                    self.game_ended = True
                    self.print_board()
                else:
                    self.change_player()
            else:
                print("That spot is already taken!")

    def make_move_graphical(self, position):
        if not self.game_ended:
            x = floor((position - 1) / self.size)
            y = (position - 1) % self.size
            result = 0
            game_ended = 0
            made_move = False
            if self.board[x][y] == self.sign_at_start:
                self.board[x][y] = self.get_player_sign()
                made_move = True
                self.turns_used += 1
                result = self.check_winning_conditions(x, y)
                if result != 0:
                    game_ended = 1
                    self.game_ended = True
                elif self.turns_used == self.size*self.size:
                    result = "Game ended, its a draw!"
                    game_ended = 1
                    self.game_ended = True
            return game_ended, made_move, result, self.player_turn, self.get_player_sign()
