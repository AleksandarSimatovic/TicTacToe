from TicTacToeGame import TicTacToeGame


def main():
    result = 0
    while result not in {'1', '2'}:
        try:
            result = input("Choose a mode for your game. 1 for textual, 2 for graphical: ")
            if result not in {'1', '2'}:
                raise ValueError
        except ValueError:
            print("Choose 1 or 2!")
    if result == '1':
        game = TicTacToeGame()
        game.play_game_text()
    else:
        import TicTacToeGraphical


main()
