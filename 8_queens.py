def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i][col] == 1:
            return False
            
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
        
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
        
    return True

def solve_queens(board, row):
    """Recursively solve the 8-Queens Problem using backtracking"""
    n = len(board)
    if row >= n:
        return True
        
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] == 1
            
            if solve_queens(board, row + 1):
                return True
                
            board[row][col] == 0
            
    return False

def print_board(board):
    """Print the board configuration"""
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def solve_8queens():
    """Solve the 8-Queens Problem and print the solution"""
    n = 8 
    board = [[0] * n for _ in range(n)]
    
    if solve_queens(board, 0):
        print("Solution found:\n")
        print_board(board)
    else:
        print("No solution exists.")

solve_8queens()