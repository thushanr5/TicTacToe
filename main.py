# Tic-Tac-Toe Project
from array import *

# board creation
board = [['-', '-', '-', ], ['-', '-', '-', ], ['-', '-', '-', ]]


def boardCreation():
    # iterating through the board to create a visualization of it
    for x in board:
        for y in x:
            print(y, end=" ")
        print()


# firstUser
def intro():
    print(f'Welcome to the game player One, please enter your name: ')
    x_user = str(input())
    print("Welcome to the game " + str(x_user))

    print(f'Welcome to the game player Two, please enter your name: ')
    y_user = str(input())
    print("Welcome to the game " + str(y_user))

    # create the Board after the intro
    boardCreation()


def x_move():
    print("What is your choice of x-coordinate player One")
    moveX_x_coordinate = int(input())

    print("What is your choice of y-coordinate player One")
    moveX_y_coordinate = int(input())

    print('Your chosen board position is ' + "[" + str(moveX_x_coordinate) + "]" + "[" + str(moveX_y_coordinate) + "]")

    board[moveX_x_coordinate][moveX_y_coordinate] = 'X'

    boardCreation()


def y_move():
    print("What is your choice of x-coordinate playerTwo")
    moveY_x_coordinate = int(input())

    print("What is your choice of y-coordinate playerTwo")
    moveY_y_coordinate = int(input())

    print('Your chosen board position is ' + "[" + str(moveY_x_coordinate) + "]" + "[" + str(moveY_y_coordinate) + "]")

    board[moveY_x_coordinate][moveY_y_coordinate] = 'O'

    boardCreation()


# TODO
# later
# board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or (
#            board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or (
#            board[2][0] == 'O' or board[2][1] == 'O' or board[2][2] == 'O') or (

def complete_game():
    if ((board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or
            (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or
            (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or

            (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or
            (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or
            (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or

            (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or
            (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X')):
        print(f'player one has won hooray ')
        return True

    elif ((board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or
          (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or
          (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or

          (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or
          (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or
          (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or

          (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or
          (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O')):
        print(f'player two has won hooray')
        return True


# def legal_board_moves():
#
#     if(board[][])

# playGame
# add conditions for if board is full or game is complete

# board size
rows = len(board)
cols = len(board[0])
total_size = rows * cols

intro()
while True:
    x_move()
    if complete_game():
        break
    y_move()
    if complete_game():
        break
