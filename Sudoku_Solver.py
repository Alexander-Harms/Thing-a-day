#TODONE: Solve Sudoku games
import time

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

def Find_Empty_Cell(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None, None

def Valid_Move(value, row, column):
    return value not in Get_Row(row) and value not in Get_Column(column) and value not in Get_Box(row - row % 3, column - column % 3)


def Solve_Puzzle(puzzle):
    row, column = Find_Empty_Cell(puzzle)
    if row == None:
        return True
    for i in range(1, 10):
        if Valid_Move(i, row, column):
            puzzle[row][column] = i
            if Solve_Puzzle(puzzle):
                return True
            puzzle[row][column] = 0
    return False

def Print_Puzzle():
    print("\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("―――――――――――――――――――――――")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(puzzle[i][j], end = ' ')
        print()




def main():
    Print_Puzzle()
    Solve_Puzzle(puzzle)
    Print_Puzzle()


if __name__ == '__main__':
    main()