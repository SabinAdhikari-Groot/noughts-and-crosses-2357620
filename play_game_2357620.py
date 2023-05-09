"""Imported all the functions and elements from noughtsandcrosses python file"""
from noughtsandcrosses_2357620 import *

def main():
    """This is the main function of this game."""
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
        print('Your current score is:', total_score)
        if choice == '2':
            save_score(total_score)
            total_score = 0
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            return
#calling the main function
if __name__ == '__main__':
    main()
