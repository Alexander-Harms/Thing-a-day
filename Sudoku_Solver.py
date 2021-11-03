#TODO: Solve Sudoku games

puzzle = [
    [0,0,0,0,6,0,0,5,8],
    [0,5,2,0,0,9,0,7,4],
    [0,7,8,0,0,0,0,0,0],
    [0,3,0,4,9,0,5,8,0],
    [0,0,5,0,0,0,4,0,7],
    [0,6,7,0,8,3,0,0,2],
    [0,2,0,9,3,0,8,6,5],
    [0,0,9,0,0,8,0,0,3],
    [3,8,0,0,4,5,0,9,1]
]

def Get_Cell(row, column):
    return puzzle[row][column]

def Get_Row(row):
    return puzzle[row]

def Get_Column(column):
    return [row[column] for row in puzzle]

def Get_Box(row, column):
    box = []
    for i in range(3):
        for j in range(3):
            box.append(puzzle[i + row][j + column])
    return box

def Check_Row(row):
    return len(set(row)) == 9

def Check_Column(column):
    return len(set(column)) == 9

def Check_Box(row, column):
    return len(set(Get_Box(row, column))) == 9

def Find_Empty_Cell(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == 0:
                return i, j

def Valid_Move(value, row, column):
    return value not in Get_Row(row) and value not in Get_Column(column) and value not in Get_Box(row - row % 3, column - column % 3)

