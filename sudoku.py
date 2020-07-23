import csv
import random

# Randomize game selection
BOARDNUM = 1 #random.randint(1,10)

# Pull the game from database
with open('game_database_short.csv') as database:
    reader = csv.reader(database)
    current_line = 0
    for line in reader:
        if current_line == BOARDNUM:
            board = line[0]
            solution = line[1]
            break
        current_line += 1