def print_grid(grid):
    """Pretty-print the Sudoku grid."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()


def find_empty(grid):
    """Find an empty cell (0 = empty). Return (row, col) or None if full."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_valid(grid, num, pos):
    """Check if num can be placed at pos (row, col)."""
    row, col = pos

    # Row check
    if num in grid[row]:
        return False

    # Column check
    if num in [grid[i][col] for i in range(9)]:
        return False

    # 3x3 subgrid check
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False

    return True


def load_puzzle_from_file(filename):
    """Load a Sudoku puzzle from a text file."""
    grid = []
    try:
        with open(filename, "r") as f:
            for line in f:
                row = [int(x) for x in line.split()]
                if len(row) != 9:
                    raise ValueError("Each row must have 9 numbers.")
                grid.append(row)
        if len(grid) != 9:
            raise ValueError("Puzzle must have 9 rows.")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        return None
    except Exception as e:
        print("❌ Error loading puzzle:", e)
        return None
    return grid
