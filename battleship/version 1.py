from random import randint

# Initialize the board and set variables
board = []
n = 5  # board size, n x n
r = 4  # number of guesses

# Creates the list used for our board
for x in range(n):
    board.append(["O"] * n)


# Creates the shape of the board as a true n x n block
def print_board(board):
    for row in board:
        print(" ".join(row))


# The next two generate the location of our battleship
def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


# Assign a variable to the location of our battleship
ship_row = random_row(board)
ship_col = random_col(board)

# Begin the games!
print("Let's play battleship! \n")
print_board(board)
print("\n")
turn = 0

for turn in range(r):
    if turn == (r - 1):  # Notifies the player what turn it is, and reminds the user if it is a last turn.
        print("Turn", turn + 1, "-- Last Turn!")
    else:
        print("Turn", turn + 1)

    guess_row = int(input("Guess Row (0-" + str(n - 1) + "): "))  # Take input for row and column
    guess_col = int(input("Guess Col (0-" + str(n - 1) + "): "))
    print("\n")

    if guess_row == ship_row and guess_col == ship_col:  # direct hit, congrats!
        print("Congratulations! You sunk my battleship! \n")
        break
    elif (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):  # miss case where guess is off board
        print("Oops, that's not even in the ocean. \n")
        print_board(board)
    elif (board[guess_row][guess_col] == "X"):  # miss case where guess was already made
        print("You guessed that one already. \n")
        print_board(board)
    else:  # all other guesses are a miss
        print("You missed my battleship! \n")
        board[guess_row][guess_col] = "X"
        print_board(board)

    # On the last turn tell the user it's game over!
    if turn == (r - 1):
        print("\n Game Over \n")

    print("\n")
