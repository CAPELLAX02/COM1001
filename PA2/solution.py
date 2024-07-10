def print_board(board):
    for row in board:
        row_str = ""
        for cell in row:
            row_str += cell + " "
        print(row_str[:-1])
    print("\n*****\n")


def enlarge_board(board, win_type, win_index):
    enlarged = ""
    for i in range(len(board)):
        line = ""
        for j in range(len(board[i])):
            cell = board[i][j]
            for _ in range(3):
                if (win_type == 'line' and i == win_index) or \
                   (win_type == 'column' and j == win_index) or \
                   (win_type == 'diagonal' and ((win_index == 1 and i == j) or (win_index == 2 and i + j == 2))):
                    line += cell
                else:
                    line += cell
            line += '-'
        enlarged += (line[:-1] + "\n") * 3
        if i < len(board) - 1:
            enlarged += '-' * 11 + "\n"
    enlarged = enlarged.rstrip('\n')
    print("Bigger size of final board is shown below\n")
    print(enlarged)
    
def check_winner(board, player):
    for i in range(3):
        row_win = True
        column_win = True
        for j in range(3):
            if board[i][j] != player:
                row_win = False
            if board[j][i] != player:
                column_win = False
        if row_win:
            return ('line', i)
        if column_win:
            return ('column', i)
    diagonal_win_1 = diagonal_win_2 = True
    for i in range(3):
        if board[i][i] != player:
            diagonal_win_1 = False
        if board[i][2-i] != player:
            diagonal_win_2 = False
    if diagonal_win_1:
        return ('diagonal', 1)
    if diagonal_win_2:
        return ('diagonal', 2)
    return (None, None)

def tic_tac_toe():
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'x'
    for move_count in range(9):
        try:
            move = input().split()
            row, col = int(move[0]), int(move[1])
            symbol = move[2]
        except (ValueError, IndexError):
            print("Invalid input.")
            continue
        if symbol != current_player or board[row][col] != '-':
            print("Invalid move or space taken. Please try again.")
            continue
        board[row][col] = current_player
        print_board(board)
        win_type, win_index = check_winner(board, current_player)
        if win_type:
            win_message = f"Game ended with {win_type} {win_index + 1}" if win_type != 'diagonal' else "Game ended with diagonal"
            print(win_message)
            print(f"Player{1 if current_player == 'x' else 2} won the game!\n")
            enlarge_board(board, win_type, win_index)
            return
        current_player = 'o' if current_player == 'x' else 'x'
    print("Tie!\n")
    enlarge_board(board, None, None)

tic_tac_toe()
