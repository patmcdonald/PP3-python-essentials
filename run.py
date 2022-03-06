# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Battleship command line game
# import randint module
# 
# from random import randint

# # single row game to start - keep it simple and build up..
# battleship = randint(0, 7)
# board = ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']

# print("BATTLESHIP!")

# SHOT = 1
# while SHOT < 5:
#     print(board)
#     guess = int(input("Guess where the Enemy Ship is: "))
#     if guess == battleship:
#         print("Direct Hit!")
#         break
#     else:
#         print("You missed! RELOAD!")
#         board[guess - 1] = "X"
#         SHOT = SHOT + 1

# Code above parked for now! \\\\

# 
# Code is adapted from https://trinket.io/python/051179b6d3
# 


from random import randint

# declare gameboard variable
board = []

for x in range(8):
    board.append(["w"] * 8)

def print_board(board):

    for row in board:
        print((" ").join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) -1 )

def random_col(board):
    return randint(0, len(board[0]) -1 )

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(8):
    print("FIRE!"), turn
    guess_row = int(input("Enter Row(0 - 7) to Aim: "))
    guess_col = int(input("Enter Column(0 - 7) to Aim: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("DIRECT HIT!")
        break
    else:
        if(guess_row <0 or guess_row >7) or (guess_col <0 or guess_col >7):
            print("Shot out of Battlezone.")
        elif(board[guess_row][guess_col] == "X"):
            print("Shot taken already!")
        else:
            print("You missed. RELOAD!")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("Battle Over!")
    turn =+ 1
    print_board(board)





# ship positions on board
def load_ships(board):
    pass
# input for gameplay - validated
def player_input():
    pass
# hit/miss alert
def alert():
    pass

# game score and results
def score():
    pass
# main method
# if __name__ == '__main__':

#    def print_board(board)

# main()