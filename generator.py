import random
from solver import solve
from utils import print_grid

def valid_in_row(grid, row, num):
    return num not in grid[row]

def valid_in_col(grid, col, num):
    return all(grid[r][col] != num for r in range(9))

def valid_in_box(grid, row, col, num):
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False
    return True

def is_safe(grid, row, col, num):
    return valid_in_row(grid, row, num) and valid_in_col(grid, col, num) and valid_in_box(grid, row, col, num)

def fill_grid(grid):
    """Fill an empty grid with a valid complete Sudoku using backtracking."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                random_nums = list(range(1, 10))
                random.shuffle(random_nums)
                for num in random_nums:
                    if is_safe(grid, i, j, num):
                        grid[i][j] = num
                        if fill_grid(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def remove_numbers(grid, clues=30):
    """Remove numbers randomly to create a puzzle (default ~30 clues)."""
    puzzle = [row[:] for row in grid]  # copy
    attempts = 81 - clues
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            attempts -= 1
    return puzzle

def generate_puzzle(clues=30):
    """Generate a random Sudoku puzzle with given number of clues."""
    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)  # make full solution
    puzzle = remove_numbers(grid, clues=clues)
    return puzzle, grid  # return puzzle and solution

if __name__ == "__main__":
    puzzle, solution = generate_puzzle(clues=35)
    print("🔢 Random Sudoku Puzzle:")
    print_grid(puzzle)
    print("\n✅ Solution:")
    print_grid(solution)
