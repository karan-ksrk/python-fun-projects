board = [
        [0, 0, 4, 3, 0, 0, 2, 0, 9], 
        [0, 0, 5, 0, 0, 9, 0, 0, 1], 
        [0, 7, 0, 0, 6, 0, 0, 4, 3],
        [0, 0, 6, 0, 0, 2, 0, 8, 7],
        [1, 9, 0, 0, 0, 7, 4, 0, 0],
        [0, 5, 0, 0, 8, 3, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 1, 0, 5], 
        [0, 0, 3, 5, 0, 8, 6, 9, 0],
        [0, 4, 2, 9, 1, 0, 3, 0, 0]
]

def show_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j==8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j) # row and column
    return None

def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
       
    # check column
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # check box
    box_y = pos[0] // 3  #row of block
    box_x = pos[1] // 3 # column of block
    
    for i in range(box_y *3, box_y*3 +3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j)!= pos:
                return False
    return  True

def solve_board(board):
    # print(board)
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve_board(board):
                return True    
    
            board[row][col] = 0
    return False

show_board(board)
solve_board(board)
print("*********************************")
show_board(board)

def set_sudoku(filename):
    import csv
    quizzes = []
    solutions = []
    with open(filename, "r")as csvfile:
        csvread = csv.reader(csvfile)
        next(csvread)
        for row in csvread:
            quizzes.append(row[0])
            solutions.append(row[1])
    return (quizzes, solutions)

def make_board(data):
    board = []
    for i in range(9):
        board.append(list((int(data[i*9+j])) for j in range(9)))
    return board

def run_random(quizzes, solutions):
    import random
    i = random.randint(0, 1000000)
    board = make_board(quizzes[i])
    solution = make_board(solutions[i])

    show_board(board)
    print("************************")
    show_board(solution)
    solve_board(board)
    print("************************")
    show_board(board)
quizzes, solutions =  set_sudoku("sudoku.csv")
run_random(quizzes, solutions)



