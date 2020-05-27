from random import randint

boardOne = []
boardTwo = []

for x in range(3):
    boardOne.append(["O"] * 3)
    boardTwo.append(["O"] * 3)

def print_boardOne(boardOne):
    for row in boardOne:
        print((" ").join(row))

def print_boardTwo(boardTwo):
    for row in boardTwo:
        print((" ").join(row))        

print("Let's play Battleship!")

print("Computer One: ")

print_boardOne(boardOne)

def random_row(boardOne):
    return randint(0, len(boardOne) - 1)
def random_col(boardOne):
    return randint(0, len(boardOne[0]) - 1)

ship_row = random_row(boardOne)
ship_col = random_col(boardOne)

print(ship_row, ship_col)

print("Computer Two: ")

print_boardTwo(boardTwo)

def random_rowTwo(boardTwo):
    return randint(0, len(boardTwo) - 1)
def random_colTwo(boardTwo):
    return randint(0, len(boardTwo[0]) - 1)

ship_rowTwo = random_rowTwo(boardTwo)
ship_colTwo = random_colTwo(boardTwo)

print(ship_rowTwo, ship_colTwo)

for turn in range(9):
    print ("Turn"), turn

    rndGuessCol = randint(0, len(boardOne) - 1)
    rndGuessRow = randint(0, len(boardOne[0]) - 1)

    guess_row = rndGuessRow
    guess_col = rndGuessRow

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations ComputerTwo! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 2) or (guess_col < 0 or guess_col > 2):
            print("Oops, that's not even in the ocean.")
        elif(boardOne[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            boardOne[guess_row][guess_col] = "X"
    if turn == 8:
        print("Game Over")
    turn =+ 1
    print("Computer One: ")
    print_boardOne(boardOne)

for turnTwo in range(9):
    print ("Turn"), turnTwo

    rndGuessCol = randint(0, len(boardTwo) - 1)
    rndGuessRow = randint(0, len(boardTwo[0]) - 1)

    guess_row = rndGuessRow
    guess_col = rndGuessRow

    if guess_row == ship_rowTwo and guess_col == ship_colTwo:
        print("Congratulations ComputerOne! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 2) or (guess_col < 0 or guess_col > 2):
            print("Oops, that's not even in the ocean.")
        elif(boardTwo[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            boardTwo[guess_row][guess_col] = "X"
    if turnTwo == 8:
        print("Game Over")
    turnTwo =+ 1
    print("Computer Two: ")
    print_boardTwo(boardTwo)