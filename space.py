import math

class Space:
    def __init__(self, value, column, row):
        self.value = value
        self.column = column
        self.row = row
        self.sector = (math.ceil(row/3)-1)*3 + math.ceil(column/3)
        if value == 0:
            self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.possibilities = []