# Game Intro
print('Hello, welcome to the Rock-Paper-Scissors game.')
user_one = input('Player 1: What is your name? ') 
user_two = input('Player 2: What is your name? ') 
print(f'Our game will consist of five rounds. {user_one} will go first and {user_two} will got second. The player that wins the most rounds will be the winner')

# Game Logic
def game():
    user_one_score = 0
    user_two_score = 0
    ties = 0
    rounds = [1, 2, 3, 4, 5]

    for round in rounds: 
        print(f'Welcome to round {round}!')

        one_choice = input(f'{user_one}, do you choose rock, paper, or scissors? ')
        two_choice = input(f'{user_two}, do you choose rock, paper, or scissors? ')

        if (one_choice == 'rock' and two_choice == 'paper') or (one_choice == 'paper' and two_choice == 'scissors') or (one_choice == 'scissors' and two_choice == 'rock'):
            print(f'{user_two} wins! {two_choice} beats {one_choice}')
            user_two_score += 1
            round += 1
        elif (one_choice == 'paper' and two_choice == 'rock') or (one_choice == 'scissors' and two_choice == 'paper') or (one_choice == 'rock' and two_choice == 'scissors'):
            print(f'{user_one} wins! {one_choice} beats {two_choice}')
            user_one_score += 1
            round += 1
        elif (one_choice == 'rock' and two_choice == 'rock') or (one_choice == 'paper' and two_choice == 'paper') or (one_choice == 'scissors' and two_choice == 'scissors'):
            print(f'We have a tie! You both chose {one_choice}')
            ties += 1
            round += 1

    if user_one_score > user_two_score:
        print(f'{user_one} has won the game!')
    elif user_two_score > user_one_score:
        print(f'{user_two} has won the game!')
    elif user_one_score == user_two_score:
        print('You have tied the game!')

game()