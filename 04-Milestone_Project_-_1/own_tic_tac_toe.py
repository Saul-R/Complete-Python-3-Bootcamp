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


def input_move(board,player):
    """
    Inputs a movement on the board for a player
    :param board: The tictactoe board
    :param player: The player's symbol
    :return: The board with the new movenment
    """
    position = input('Input the position on the board: ')
    board[position] = player
    return board


def check_game_status(board):
    return (rows_match(board)) or (columns_match(board)) or (diagonals_match(board))


def cells_match(cell1, cell2, cell3):
    return (cell1 == cell2) and (cell2 == cell3)


def rows_match(board):
    row1 = cells_match(board[1], board[2], board[2])
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
    diag2 = cells_match(board[4], board[5], board[6])
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
    print("| {} | {} | {} |".format(board[1],board[2],board[3]))
    print("| {} | {} | {} |".format(board[4],board[5],board[6]))
    print("| {} | {} | {} |".format(board[7],board[8],board[9]))
    print("-------------")


def check_tie(board):
    return not any(x == " " for x in board.values())


def play_a_game(board):
    players = ['X', 'O']
    while True:
        for player in players:
            board = input_move(board,player)
            winner = check_winner(board)
            if winner:
                print('The player {} has won!')
                break
            tie = check_tie(board)
            if tie:
                print('Cannot do any movement. This is a tie')
                break


if __name__=="main":
    board = create_board()
    keep_playing = True
    while keep_playing:
        play_a_game(board)
        keep_playing = input('Keep playing? (True / False): ')
    print('Thanks for playing.')
