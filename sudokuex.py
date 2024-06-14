import random
board=[[0]*9 for _ in range(9)]
def initialize_board():
    return board

def display_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-'*21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            print(board[i][j], end=' ')
        print()

def is_valid_move(board, row, col, num):
    # Check if num is not already in the same row
    if num in board[row]:
        return False
    
    # Check if num is not already in the same column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if num is not already in the same 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_valid_puzzle(board):
    # Fill diagonal blocks with random numbers
    for i in range(0, 9, 3):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers)
        for j in range(3):
            for k in range(3):
                board[i+j][i+k] = numbers.pop()
    
    # Solve the board to get a valid puzzle
    solve_sudoku(board)
    #Difficulty Level
    num=int(input("Enter difficulty level from 1 to 5:"))
    if num>5:
        print("Hold on smarty pants!(Level limit exceeded.)")
        num=5
    elif num<1:
        print("How big of a noob are you?")
        num=1
    else:
        print("Enter a number between 1 and 5.")

    # Remove numbers to make the puzzle
    for _ in range(num*11):  # Adjust this number for puzzle difficulty
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        board[row][col] = 0

def play_sudoku(board):
    while True:
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))

        if is_valid_move(board, row, col, num):
            board[row][col] = num
            display_board(board)
            if all(0 not in row for row in board):
                print("Congratulations! You solved the puzzle!")
                break
        
        else:
            print("Invalid move! Try again.")

def choice():

    x= int(input("Enter a choice(0 to play or 1 to solve):"))
    if x== 0:
        play_sudoku(board)
    elif x==1:
        solve_sudoku(board)
    else:
        print("Invalid choice")

def main():

    print("Hola amigo!")
    name=input("What would you like me to call you? :")
    print("Lessgoooo", name)
    board = initialize_board()
    generate_valid_puzzle(board)
    display_board(board)
    choice()
    display_board(board)

if __name__ == "__main__":
    main()
