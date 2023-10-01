def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def placeQueens(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1

            if placeQueens(board, col + 1, N) == True:
                return True

            board[i][col] = 0  # Backtrack if placing a queen doesn't lead to a solution

    return False

def solveNQueensProblem(N):
    board = [([0]*N) for i in range(N)]

    if placeQueens(board, 0, N) == False:
        print("Solution does not exist")
        return

    printSolution(board, N)

solveNQueensProblem(8)
