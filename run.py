# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Battleship command line game

# declare gameboard variable
gameboard = []
for x in range(0, 8):
    gameboard.append(['w'] * 8)

"""
Prints the Battleship gameboard
"""
def print_gameboard(gameboard):
    for row in gameboard:
        print(" ").join(row)

    print(gameboard)

# ship positions on board
def load_ships():
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
if __name__ == '__main__':

    print_gameboard(gameboard)

    main()