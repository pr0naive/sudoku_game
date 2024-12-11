# sudoku_game


1. Fill Diagonal Blocks: Start by filling the diagonal blocks (3x3 squares) with random numbers. Ensure that each number appears exactly once in each block.

2. Backtracking Algorithm: Use a backtracking algorithm to fill the remaining empty cells. Start from the top-left cell and recursively try different numbers until a solution is found.

3. Ensure Uniqueness: To ensure the puzzle has a unique solution, try removing numbers one by one and checking if the puzzle still has a unique solution. If it does, remove the number, otherwise, leave it.
