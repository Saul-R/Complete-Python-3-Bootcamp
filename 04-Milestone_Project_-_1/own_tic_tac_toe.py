def create_board():
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
    pass

def input_move():
    pass

def check_game_status():
    pass

def print_board(board):
    '''
    Receives a tictactoe board and prints it.
    :param board: The board dictionary
    :return: void
    '''
    print("---------")
    print("{} | {} | {}".format(board[1],board[2],board[3]))
    print("{} | {} | {}".format(board[4],board[5],board[6]))
    print("{} | {} | {}".format(board[7],board[8],board[9]))
    print("---------")

def print_winner():
    pass

def print_finish():
    pass

def print_tie():
    pass

def play_a_game():
    while True:
        input=input_move()
        print_board()
        game_status=check_game_status(board)
        if game_status == 'Winner':
            print_winner()
            break
        elif game_status == 'Tie'
            print_tie()

if __name__=="main"

    create_board()
    keep_playing = True

    while keep_playing == True:
        play_a_game()
        keep_playing=input_replay()
    print_finish()