import time
from solver import solve
from utils import print_grid
from generator import generate_puzzle

def main():
    # Generate a random puzzle each run
    puzzle, solution = generate_puzzle(clues=35)  # change clues for difficulty

    print("🔢 Random Sudoku Puzzle:")
    print_grid(puzzle)

    # Wait 5 seconds before solving
    print("\n⏳ Solving in 5 seconds...")
    time.sleep(5)

    print("\n✅ Solved Sudoku (by solver):")
    if solve(puzzle):
        print_grid(puzzle)
    else:
        print("❌ No solution found (should not happen).")

if __name__ == "__main__":
    main()
