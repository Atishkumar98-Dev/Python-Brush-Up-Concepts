# X and 0 game 
#Board
#Display Board
#Continue Game Switch Player
#Break Game Win or Draw
#Cross /Column / Diagonal for Win

board = ['-','-','-',
         '-','-','-',
         '-','-','-',
         ]

game_still_going = True
current_player = "X"
winner = None


def display_board():
    print(board[0]+ '|' + board[1] + '|' + board[2])
    print(board[3]+ '|' + board[4] + '|' + board[5])
    print(board[6]+ '|' + board[7] + '|' + board[8])

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = 'X'
    return


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        flip_player()
        check_if_game_over()


def handle_turn(player):
    position = input("Choose a number from 1 to 9")
    position = int(position) - 1
    board[position] = player
    display_board()




def check_if_win():
    # ROw
    global winner
    global game_still_going
    row_1 =  board[0] == board[1] == board[2] != '-'
    row_2 =  board[3] == board[4] == board[5] != '-'
    row_3 =  board[6] == board[7] == board[8] != '-'
    col_1 =  board[0] == board[3] == board[6] != '-'
    col_2 =  board[1] == board[4] == board[7] != '-'
    col_3 =  board[2] == board[5] == board[8] != '-'
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[6] == board[4] == board[2] != '-'
    if row_1 or row_2 or row_3:
        winner = current_player
        print(winner,'Won By Sequnce in Row')
        game_still_going = False
    if col_1 or col_2 or col_3:
        winner = current_player
        print(winner,'Won By Sequnce in Column')
        game_still_going = False
    if diag_1 or diag_2:
        winner = current_player
        print(winner,'Won By Sequnce in Diagonal')
        game_still_going = False
    # check rows/Column/Diagonal2
    return 


def check_if_tie():
    if '-' not in board:
        print("TIE!")
    return



def check_if_game_over():
    check_if_win()
    check_if_tie()


play_game()