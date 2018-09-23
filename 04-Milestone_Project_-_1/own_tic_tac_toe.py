def create_board():
    """
    Creates empty board
    :return: Dictionary with new tictactoe board
    """
    board={
        1: " ",
        2: " ",
        3: " ",
        4: " ",
        5: " ",
        6: " ",
        7: " ",
        8: " ",
        9: " "
    }
    return board


def input_replay():
    return True


def input_move(board, player):
    """
    Inputs a movement on the board for a player
    :param board: The tictactoe board
    :param player: The player's symbol
    :return: The board with the new movenment
    """
    input_validated = False
    while not input_validated:
        position = input('Player {}: Input the position on the board: '.format(player))
        try:
            if (int(position) in board.keys()) and (board[int(position)] == " "):
                board[int(position)] = player
                input_validated = True
            else:
                print("Wrong input, try again")
        except ValueError:
            print("Wrong input type, use a number 1 to 9. Try again")

    return board


def check_winner(board):
    return (rows_match(board)) or (columns_match(board)) or (diagonals_match(board))


def cells_match(cell1, cell2, cell3):
    return (cell1 == cell2) and (cell2 == cell3) and (cell1 != " ")


def rows_match(board):
    row1 = cells_match(board[1], board[2], board[3])
    row2 = cells_match(board[4], board[5], board[6])
    row3 = cells_match(board[7], board[8], board[9])
    return row1 or row2 or row3

def columns_match(board):
    col1 = cells_match(board[1], board[4], board[7])
    col2 = cells_match(board[2], board[5], board[8])
    col3 = cells_match(board[3], board[6], board[9])
    return col1 or col2 or col3


def diagonals_match(board):
    diag1 = cells_match(board[1], board[5], board[9])
    diag2 = cells_match(board[7], board[5], board[3])
    return diag1 or diag2


def print_board(board):
    """
    Receives a tictactoe board and prints it.
    :param board: The board dictionary
    :return: void
    """
    print("-------------")
    print("--  BOARD  --")
    print("-------------")
    print("| {} | {} | {} |".format(board[7], board[8], board[9]))
    print("| {} | {} | {} |".format(board[4], board[5], board[6]))
    print("| {} | {} | {} |".format(board[1], board[2], board[3]))
    print("-------------")


def check_tie(board):
    return not any(x == " " for x in board.values())


def play_a_game(board):
    players = ['X', 'O']
    game_continues = True
    while game_continues:
        for player in players:
            board = input_move(board, player)
            print_board(board)
            winner = check_winner(board)
            if winner:
                print('The player {} has won!'.format(player))
                game_continues = False
                break
            tie = check_tie(board)
            if tie:
                print('Cannot do any movement. This is a tie')
                game_continues = False
                break
    print("Game finished!")


if __name__ == "__main__":
    board = create_board()
    keep_playing = "yes"
    while keep_playing == "yes":
        print_board(board)
        play_a_game(board)
        keep_playing = input('Play Again? (yes / no): ')
        print('Keep playing: '.format(keep_playing))
        board = create_board()
    print('Thanks for playing.')
