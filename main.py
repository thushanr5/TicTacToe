# Tic-Tac-Toe Project

from array import *

# board creation
board = [['-', '-', '-', ], ['-', '-', '-', ], ['-', '-', '-', ]]


def board_creation():
    # iterating through the board to create a visualization of it
    for x in board:
        for y in x:
            print(y, end=" ")
        print()


# introduction to the game to welcome both players
def intro():
    print(f'Welcome to the game player One, please enter your name: ')
    x_user = str(input())
    print("Welcome to the game " + str(x_user))

    print(f'Welcome to the game player Two, please enter your name: ')
    y_user = str(input())
    print("Welcome to the game " + str(y_user))

    # create the Board after the intro
    board_creation()


def x_move():
    print("What is your choice of x-coordinate player One")
    moveX_x_coordinate = int(input())

    # checking is move is valid in the x direction
    while moveX_x_coordinate > 2 or moveX_x_coordinate < 0:
        print(f'Please choose another position for the x-coordinate')
        moveX_x_coordinate = int(input())

    print("What is your choice of y-coordinate player One")
    moveX_y_coordinate = int(input())

    # checking is move is valid in the y direction
    while (moveX_y_coordinate > 2 or moveX_y_coordinate < 0) or board[moveX_x_coordinate][moveX_y_coordinate] == 'O' or board[moveX_x_coordinate][moveX_y_coordinate] == 'X':
        print(f'Please choose another position for the y-coordinate')
        moveX_y_coordinate = int(input())

    print('Your chosen board position is ' + "[" + str(moveX_x_coordinate) + "]" + "[" + str(moveX_y_coordinate) + "]")

    board[moveX_x_coordinate][moveX_y_coordinate] = 'X'

    board_creation()


def y_move():
    print("What is your choice of x-coordinate playerTwo")
    moveY_x_coordinate = int(input())

    # checking is move is valid in the x direction
    while moveY_x_coordinate > 2 or moveY_x_coordinate < 0:
        print(f'Please choose another position for the x-coordinate')
        moveY_x_coordinate = int(input())

    print("What is your choice of y-coordinate playerTwo")
    moveY_y_coordinate = int(input())

    # checking is move is valid in the y direction
    while (moveY_y_coordinate > 2 or moveY_y_coordinate < 0) or board[moveY_x_coordinate][moveY_y_coordinate] == 'X' or board[moveY_x_coordinate][moveY_y_coordinate] == 'O':
        print(f'Please choose another position for the y-coordinate')
        moveY_y_coordinate = int(input())

    print('Your chosen board position is ' + "[" + str(moveY_x_coordinate) + "]" + "[" + str(moveY_y_coordinate) + "]")

    board[moveY_x_coordinate][moveY_y_coordinate] = 'O'

    board_creation()


def complete_game():
    # all winnable positions -> X-player
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

        # all winnable positions -> O-player
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

        # full board X or o player -> No one has won
    elif ((board[0][0] != '-' and board[0][1] != '-' and board[0][2] != '-') and
          (board[1][0] != '-' and board[1][1] != '-' and board[1][2] != '-') and
          (board[2][0] != '-' and board[2][1] != '-' and board[2][2] != '-')):
        print(f'No One Has Won the Game')
        return True


# play Game
intro()
while True:
    x_move()
    if complete_game():
        break
    y_move()
    if complete_game():
        break
