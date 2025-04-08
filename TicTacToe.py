import os

def check_w(board):
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] and board[i*3] != ' ':
            return board[i*3]
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return board[i]
    
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]

    return None
    
def draw(board):
    return all(cell != ' ' for row in board for cell in row)
        

def print_ttt(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        print('---+---+---') if i < 2 else None

def ttt():
    os.system('cls')
    board = [" " for _ in range(9)]
    players = ['O', 'X']
    cp = 0

    print('Start Tic Tac Toe Game')
    print('======================')
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        print(f"\nPlayer {players[cp]}'s turn:")
        a = int(input(f"Enter cell number (1-9): ")) - 1
        i = a // 3
        j = a % 3
        if not (0 <= i < 3 and 0 <= j < 3):  
            print("Invalid input.")
            continue

        if board[a] != ' ':
            print("Cell is already taken.")
            continue

        board[a] = players[cp]
        os.system('cls')
        print('Start Tic Tac Toe Game')
        print('======================')
        print_ttt(board)

        w = check_w(board)
        if w:
            print(f"\nPlayer {w} Wins!")
            break
        if draw(board):
            print("\nIt\'s a Draw.")
            break
        
        cp = 1 - cp

ttt()
