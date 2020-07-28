import csv
import random
from space import Space

BOARDNUM = random.randint(1,10) # Randomize game selection
board = []
board_list = []
solution_list = []

# Pull the game from database
def get_game():
    with open('game_database_short.csv') as database:
        reader = csv.reader(database)
        current_line = 0
        for line in reader:
            if current_line == BOARDNUM:
                for n in line[0]:
                    board_list.append(n)
                for n in line[1]:
                    solution_list.append(n)
                break
            current_line += 1
    column = 1
    row = 1
    while row <= 9:
        while column <= 9:
            board.append(Space(int(board_list[((column + (row-1)*9))-1]), column, row))
            column += 1
        column = 1
        row += 1

# Solve
def solve():
    i = 0
    for space_beeing_checked in board:
        if space_beeing_checked.value == 0:
            for space in board:
                if (space_beeing_checked.row == space.row) or (space_beeing_checked.column == space.column) or (space_beeing_checked.sector == space.sector):
                    if space.value in space_beeing_checked.possibilities:
                        space_beeing_checked.possibilities.remove(space.value)
                        if len(space_beeing_checked.possibilities) == 1:
                            space_beeing_checked.value = space_beeing_checked.possibilities[0]

                            break
        i += 1

# Check if it is solved
def is_solved():
    for space in board:
        if space.value == 0:
            return False
    return True

# Print board for visualization
def print_board():
    for space in board:
        print(space.value, end = " ")
        if space.column == 9:
            print()
    print()



get_game()
print("Solving game #"+str(BOARDNUM)+"\n")
print_board()

count = 0
while not is_solved():
    solve()
    count += 1

print_board()
print("Solving took "+str(count)+" attempts")