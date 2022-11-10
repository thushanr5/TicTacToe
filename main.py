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


def intro():
    print(f'Welcome to the game player One, please enter your name: ')
    x_user = str(input())
    print("Welcome to the game " + str(x_user))

    print(f'Welcome to the game player Two, please enter your name: ')
    y_user = str(input())
    print("Welcome to the game " + str(y_user))

    # create the Board after the intro
    boardCreation()




# def validate():
#     while True:
#         while board[moveX_x_coordinate] > 2 or board[moveX_x_coordinate] < 0:
#             print('please pick a x-coordinate playerOne')
#             moveX_x_coordinate = int(input())
#
#         while board[moveX_y_coordinate] > 2 or board[moveX_y_coordinate] < 0:
#             print('please pick a y-coordinate playerOne')
#             moveX_y_coordinate = int(input())
#
#         print('Your chosen board position is ' + "[" + str(moveX_x_coordinate) + "]" + "[" + str(
#             moveX_y_coordinate) + "]")
#
#         board[moveX_x_coordinate][moveX_y_coordinate] = 'X'
#
#         boardCreation()



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


def complete_game():
    if ((board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or
            (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or
            (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or

            (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or
            (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or
            (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or

            (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or
            (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X')):
        print(f'Player One Has Won Hooray! ')
        return True

    elif ((board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or
          (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or
          (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or

          (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or
          (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or
          (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or

          (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or
          (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O')):
        print(f'Player Two Has Won Hooray!')
        return True

    elif ((board[0][0] != '-' and board[0][1] != '-' and board[0][2] != '-') and
          (board[1][0] != '-' and board[1][1] != '-' and board[1][2] != '-') and
          (board[2][0] != '-' and board[2][1] != '-' and board[2][2] != '-')):
        print(f'No One Has Won the Game')
        return True


# add conditions for if board is full or game is complete

# board size
rows = len(board)
cols = len(board[0])
total_size = rows * cols

# play Game
intro()
while True:
    x_move()
    if complete_game():
        break
    y_move()
    if complete_game():
        break
