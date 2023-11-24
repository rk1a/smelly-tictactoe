import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == symbol for row in range(len(board))):
            return True

    if all(board[i][i] == symbol for i in range(len(board))) or all(
        board[i][len(board) - i - 1] == symbol for i in range(len(board))
    ):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_player_move():
    try:
        move = int(input("Enter your move (1-9): "))
        if 1 <= move <= 9:
            return move
        else:
            print("Invalid move! Enter a number between 1 and 9.")
            return get_player_move()
    except ValueError:
        print("Invalid input! Enter a number between 1 and 9.")
        return get_player_move()


def get_computer_move(board):
    available_moves = [i + 1 for i in range(9) if board[i // 3][i % 3] == " "]
    if available_moves:
        return random.choice(available_moves)
    else:
        return None


def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True

    while True:
        print_board(board)

        if player_turn:
            move = get_player_move()
            symbol = "X"
        else:
            move = get_computer_move(board)
            symbol = "O"

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] == " ":
            board[row][col] = symbol
            if check_winner(board, symbol):
                print_board(board)
                print(f"{symbol} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                player_turn = not player_turn
        else:
            print("Invalid move! Cell already taken. Try again.")


if __name__ == "__main__":
    play_tic_tac_toe()
