# Code is adapted from https://trinket.io/python/051179b6d3

from random import randint
"""Imports random integer function"""

# declare gameboard variable
board = []

for x in range(8):
    board.append(["w"] * 8)


def print_board(board):
    """Prints battlezone board to terminal"""
    for row in board:
        print((" ").join(row))


print_board(board)


def random_row(board):
    """random ship position in row"""
    return randint(0, len(board)-1)


def random_col(board):
    """random ship position in column"""
    return randint(0, len(board[0])-1)


ship_row = random_row(board)
ship_col = random_col(board)

for TURN in range(8):
    print("TAKE AIM!")
    guess_row = int(input("Enter Row(0 - 7) to Aim: "))
    guess_col = int(input("Enter Column(0 - 7) to Aim: "))
    print("FIRE!")

    if guess_row == ship_row and guess_col == ship_col:
        print("DIRECT HIT!")
        break
    else:
        if(guess_row < 0 or guess_row > 7) or (guess_col < 0 or guess_col > 7):
            print("Shot out of Battlezone.")
        elif(board[guess_row][guess_col] == "X"):
            print("Shot taken already!")
        else:
            print("You missed. RELOAD!")
            board[guess_row][guess_col] = "X"
    if TURN == 8:
        print("Battle Over!")
    TURN = + 1
    print_board(board)