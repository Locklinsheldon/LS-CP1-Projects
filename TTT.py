import random

def PrintBoard(board):
    count = 1
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                print(count, end = " ")
            else:
                print(board[row][col], end = " ")
            count += 1
        print()

def CheckWhoWon(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def AiMove(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

def PlayerMove(board):
    while True:
        try:
            ask = int(input("Which number do you want to place x on?: "))
            if ask in range(1, 10):
                row, col = divmod(ask - 1, 3)
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("This square belongs to O.")
            else:
                print("It's got to be between 1 and 9.")
        except ValueError:
            print("Wrong/Invalid input.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac's Toes")
    PrintBoard(board)

    while True:
        PlayerMove(board)
        PrintBoard(board)
        winner = CheckWhoWon(board)
        if winner:
            print(f"{winner} wons")
            break

        AiMove(board)
        PrintBoard(board)
        winner = CheckWhoWon(board)
        if winner:
            print(f"{winner} wons")
            break

if __name__ == "__main__":
    main()
