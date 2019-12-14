from random import randint

mark = ''


# Function to check whether the position is empty or not to place the mark.

def board_pos_empty_check(board, pos):
    c = 0
    for i in range(1, 10):
        if board[i] != ' ':
            c = c + 1
    if board[pos] == ' ' or c < 9:
        return True
    else:
        return False


# Function to check whether the board is full or not.

def full_board(board):
    for i in range(1, 10):
        if board_pos_empty_check(board, i):
            return False
        else:
            return True


# Function to Check the winning conditions.

def win():
    if mark == 'X' or mark == 'O':
        if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (
                board[7] == board[8] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (
                board[7] == board[5] == board[3] == mark) or (board[7] == board[4] == board[1] == mark) or (
                board[8] == board[5] == board[2] == mark) or (board[9] == board[6] == board[3] == mark):
            return True
    else:
        return False


# Function for placing the mark by two Players and to call turn change function.

def move():
    global mark
    if turn == 0:
        pos = int(input("\nChoose The position(1-9)-->"))
        if board_pos_empty_check(board, pos):
            mark = pl1
            board[pos] = mark
        turn_change(turn)
    else:

        pos = int(input("\nChoose The position(1-9)-->"))
        if board_pos_empty_check(board, pos):
            mark = pl2
            board[pos] = mark
        turn_change(turn)


# Function for changing or switching the turn from Player 1 to Player 2

def turn_change(n):
    if n == 1:
        globals()['turn'] = 0
    else:
        globals()['turn'] = 1


# Function to Print the Resultant Board after every move.

def bord():
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# Main Function to start the GAME and to call above mentioned functions.

def start():
    global board
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    global pl1, pl2, ch, turn, ch
    pl1 = ''
    pl2 = ''
    turn = randint(0, 1)
    ch = ''
    print()
    print('Welcome! to tic tac toe')
    while pl1 != 'X' and pl1 != 'O':
        pl1 = input("Player 1 choose X or O -->").upper()
    if pl1 == 'X':
        pl2 = 'O'
    else:
        pl2 = 'X'

    if turn == 0:
        print("Player 1 will start the game!")
    elif turn == 1:
        print("Player 2 will start the game!")
    print()
    bord()  # Printing the blank structure of the board.
    c = 0
    while True:
        move()
        print("\n" * 100)
        bord()
        if c > 0:
            if win():
                print()
                if turn == 1:
                    print("Player 1 Won the GAME!")
                else:
                    print("Player 2 Won the GAME!")
                break
        if full_board(board):
            print()
            print("MATCH TIE!!")
            break
        elif c == 0:
            c += 1
    print()
    replay()


# Function for asking user that if he want to replay or not?

def replay():
    ch = input("Whant to REPLAY??(y/n):")
    if ch == 'y' or ch == 'Y':
        start()
    elif ch == 'n' or ch == 'N':
        return 0
    else:
        replay()


# Calling of start function,This will initialise the GAME.

start()