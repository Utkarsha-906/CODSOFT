import math

# Constants for representing players on the board
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full (a tie)
    return all(cell != EMPTY for row in board for cell in row)

def get_empty_cells(board):
    # Get a list of empty cells on the board
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, maximizing_player):
    # Minimax algorithm with alpha-beta pruning for optimal move calculation
    if is_winner(board, PLAYER_X):
        return -1
    if is_winner(board, PLAYER_O):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    # Find the best move for the AI using the minimax algorithm
    best_val = -math.inf
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = PLAYER_O
        move_val = minimax(board, 0, False)
        board[i][j] = EMPTY
        if move_val > best_val:
            best_val = move_val
            best_move = (i, j)
    return best_move

def main():
    # Initialize the Tic-Tac-Toe board
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_X
        else:
            print("Cell already occupied. Try again.")
            continue

        print_board(board)

        if is_winner(board, PLAYER_X):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = PLAYER_O
        print_board(board)

        if is_winner(board, PLAYER_O):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
