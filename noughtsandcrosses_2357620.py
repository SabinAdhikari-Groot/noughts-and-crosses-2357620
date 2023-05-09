"""To import the random integer, check file path and encode python object"""
import random
import os.path
import json
random.seed()


def draw_board(board):
    """This function draw the noughts and crosses board."""
    print('-------------')
    print('| ' + board[0][0] + ' | ' + board[0]
          [1] + ' | ' + board[0][2] + ' |')
    print('-------------')
    print('| ' + board[1][0] + ' | ' + board[1]
          [1] + ' | ' + board[1][2] + ' |')
    print('-------------')
    print('| ' + board[2][0] + ' | ' + board[2]
          [1] + ' | ' + board[2][2] + ' | ')
    print('-------------')


def welcome(board):
    """Prints the welcome message and displays the board."""
    print("Welcome to the 'Unbeatable Noughts and Crosses' game.")
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")


def initialise_board(board):
    """This function initializes an empty board."""
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            board[i][j] = ' '
    return board


def get_player_move(board):
    """This function asks the user move and updates the board with 'X' in the selected square"""
    while True:
        move = input("Choose your square (1-9): ")
        if not move.isdigit():
            print("Please enter a digit.")
            continue
        square = int(move)
        if not 1 <= square <= 9:
            print("Enter a number from 1 to 9.")
            continue
        row = (square - 1) // 3
        col = (square - 1) % 3
        if board[row][col] != ' ':
            print("That square has already been choosen.")
            continue
        board[row][col] = 'X'
        return row, col


def choose_computer_move(board):
    """This function takes the move of computer!"""
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col


def check_for_win(board, mark):
    """This function checks whether the player or computer has won or not!"""
    for i in range(3):
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True
    for i in range(3):
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True

    return False


def check_for_draw(board):
    """This function checks whether the game is draw or not."""
    for row in board:
        if " " in row:
            return False
    return True


def play_game(board):
    """This function starts the game for playing."""
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        print(f"Player's last move was board[{row}][{col}]")
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Congratulations! You won!")
            return 1
        if check_for_draw(board):
            print("Sorry! This game is a draw.")
            return 0
        row, col = choose_computer_move(board)
        print(f"Computer's last move was board[{row}][{col}]")
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Sorry! You lose.!")
            return -1
        if check_for_draw(board):
            print("Sorry! The game is a draw.")
            return 0


def menu():
    """This function ask the player to choose one process from main menu."""
    while True:
        print("Main Menu")
        print("1. Play the game")
        print("2. Save score in file 'leaderboard.txt'")
        print("3. Load and display the scores from the 'leaderboard.txt'")
        print("q. Quit the program")
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "q"]:
            return choice


def load_scores():
    """This function loads the scores from the leaderboard text file."""
    if os.path.isfile('leaderboard.txt') and os.path.getsize('leaderboard.txt') > 0:
        with open('leaderboard.txt', 'r', encoding="utf-8") as score_file:
            try:
                leaders = json.load(score_file)
            except json.JSONDecodeError:
                print("Error in file!")
                leaders = {}
    else:
        leaders = {}
    return leaders


def save_score(score):
    """This functions saves the score of player according to name."""
    user_name = input("Enter your name: ")
    leaders = load_scores()
    if user_name in leaders:
        leaders[user_name] += score
    else:
        leaders[user_name] = score
    with open('leaderboard.txt', 'w', encoding="utf-8") as score_file:
        json.dump(leaders, score_file)


def display_leaderboard(leaders):
    """This function is used for displaying the leaderboard."""
    sorted_leaders = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
    print("Leaderboard:")
    for name, score in sorted_leaders:
        print(f"{name}: {score}")
