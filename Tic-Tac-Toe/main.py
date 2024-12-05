def draw(board):
    for i in range(5):
        if i % 2 == 0:
            row_index = i // 2
            print(f" {board[row_index * 3]} | {board[row_index * 3 + 1]} | {board[row_index * 3 + 2]} ")
        else:
            print("---+---+---")


def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return board[condition[0]]  # Return the winner ('X' or 'O')
    return None  # No winner yet


def is_draw(board):
    return all(cell == 'X' or cell == 'O' for cell in board)


# Initialize the board
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

turn = 'X'  # Start with Player X

while True:
    draw(board)
    move = int(input(f"Player {turn}, enter the cell number (1-9): ")) - 1

    if board[move] != 'X' and board[move] != 'O':  # Check if the cell is free
        board[move] = turn  # Make the move
    else:
        print("Cell is already taken, please choose another!")
        continue

    winner = check_winner(board)
    if winner:
        draw(board)
        print(f"Player {winner} wins!")
        break

    if is_draw(board):
        draw(board)
        print("It's a draw!")
        break

    # Switch turns
    turn = 'O' if turn == 'X' else 'X'
