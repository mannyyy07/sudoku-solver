from utils import find_empty, is_valid

def solve(grid):
    """Solve Sudoku using backtracking."""
    empty = find_empty(grid)
    if not empty:
        return True  # Puzzle solved

    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0  # Reset and backtrack

    return False
