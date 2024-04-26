from random import choices
from collections import defaultdict
import argparse

# Set to True to enable debug mode
DEBUG = False
# Game settings
NR_OF_GUESSES = 100
NR_OF_COLOURS = 4


def setup_game(nr_of_colours: int = 4) -> list[str]:
    '''
    This function will setup the game by generating a random code for the player to guess.
    '''
    colours = ["red", "green", "blue", "yellow", "purple", "orange"]
    code = choices(colours, k=nr_of_colours)

    if DEBUG:
        code = ['purple', 'purple', 'green', 'blue']
        print(f"DEBUG: The code is {code}")

    return code


def check_guess(code: list[str], guess: list[str]) -> bool:
    '''
    This function will check the player's guess against the code and return True if the guess is correct.
    '''
    colours_in_code = {colour: code.count(colour) for colour 
                       in ["red", "green", "blue", "yellow", "purple", "orange"]}

    if DEBUG:
        for colour in colours_in_code.keys():
            print(f"DEBUG: {colour} {colours_in_code[colour]}")

    correct = 0
    misplaced = 0

    result = ['\033[1;97;40m ████ \033[1;0;0m' for _ in range(len(code))]

    for i in range(len(code)):
        guess_color = guess[i]
        code_color = code[i]

        if guess_color == code_color:
            correct += 1
            result[i] = "\033[1;32;40m ████ \033[1;0;0m"# "Black"
            colours_in_code[guess_color] -= 1

    for i in range(len(code)):
        guess_color = guess[i]
        code_color = code[i]

        if colours_in_code[guess_color] > 0 and guess_color != code_color:
            misplaced += 1
            colours_in_code[guess_color] -= 1
            result[i] = "\033[1;33;40m ████ \033[1;0;0m"

    if DEBUG:
        print(f"DEBUG: {correct} correct, {misplaced} misplaced")
        print(f"DEBUG: {result}")

    
    return correct == len(code), result


def validate_guess(guess: list[str], length: int = 4) -> bool:
    '''
    This function will validate the player's guess.
    '''
    if len(guess) != length:
        print("You must enter exactly four colours.")
        return False
    for colour in guess:
        if colour not in ["red", "green", "blue", "yellow", "purple", "orange"]:
            print(f"{colour} is not a valid colour.")
            return False
    return True


def play_game(code: list[str], nr_of_guesses: int = 6):
    '''
    This function will play the game with the player.
    '''
    for _ in range(nr_of_guesses):
        guess = input("Enter your guess: \n").lower().split()
    
        while not validate_guess(guess, len(code)):
            guess = input("Enter a new guess please: \n").lower().split()

        correct, result = check_guess(code, guess) 
        for item in result:
            print(item, end="")
        print()
        if correct:
            print("You win!")
            print(f"The code was indeed was:\n{code}\n")
            break
        else:
            print("Incorrect, please try again!\n")
    else: # This will run if the loop completes without a break
        print(f"The code was {code}")


def simulate_game(code: list[str], length: int = 4):
    '''
    This function will simulate the game and return True if the player wins.
    '''
    options = ["red", "green", "blue", "yellow", "purple", "orange"]
    weights = [1, 1, 1, 1, 1, 1]

    known_colours = ['', '', '', '']

    for attemts in range(NR_OF_GUESSES):

        guess = choices(options, weights=weights, k=length)

        for i in range(len(code)):
            if known_colours[i] != '':
                guess[i] = known_colours[i]
        
        colours_in_code = {colour: code.count(colour) for colour 
                        in ["red", "green", "blue", "yellow", "purple", "orange"]}

        correct = 0

        result = ['not included' for _ in range(len(code))]

        for i in range(len(code)):
            guess_color = guess[i]
            code_color = code[i]

            if guess_color == code_color:
                correct += 1
                result[i] = "correct"
                colours_in_code[guess_color] -= 1

        for i in range(len(code)):
            guess_color = guess[i]
            code_color = code[i]

            if colours_in_code[guess_color] > 0 and guess_color != code_color:
                colours_in_code[guess_color] -= 1
                index = options.index(guess_color)
                weights[index] += 1
                result[i] = "misplaced"

        skip = []
        for i in range(len(code)):
            if result[i] == 'not included' and guess[i] not in skip:
                delete = guess[i]
                weights.pop(options.index(delete))
                options.remove(guess[i])
                skip.append(guess[i])

            if result[i] == 'correct':
                known_colours[i] = guess[i]

            if result[i] == 'misplaced':
                skip.append(guess[i])

        if '' not in known_colours:
            if attemts > 16:
                print(f"DEBUG: {code}")
            return True, attemts + 1
        
    return False, 'unsolved'
    

def simulate_n_iterations(iterations: int = 1000):
    '''
    This function will simulate the game n times and return the percentage of wins.
    '''
    wins = 0
    total_nr_of_guesses = defaultdict(int)
    for _ in range(iterations):
        code = setup_game(NR_OF_COLOURS)
        solved, attemts = simulate_game(code, NR_OF_COLOURS)
        total_nr_of_guesses[attemts] += 1
        if solved:
            wins += 1
    persentage = wins / iterations * 100
    print(f"Out of {iterations} games, the player won {wins} times ({persentage:.2f}%).")
    for key, value in total_nr_of_guesses.items():
        print(f"{key} guesses: {value} times.")
    average = sum([key * value for key, value in total_nr_of_guesses.items() if key != 'unsolved']) / iterations
    print(f"The average number of guesses was {average:.2f}.")


def create_parser():
    parser = argparse.ArgumentParser(description="Mastermind game")
    parser.add_argument("-s", "--simulate", metavar='simulate n times',
                        nargs=1, type=int,
                        help="Simulate the game the specified number of times.")
    return parser.parse_args()


def main():

    args = create_parser()

    if args.simulate:
        simulate_n_iterations(args.simulate[0])
        return

    while True:

        print ("Welcome to Mastermind!")
        print ("The colours are red, green, blue, yellow, purple, orange.")
        print (f"Enter your guess as {NR_OF_COLOURS} colours separated by spaces.")
        print (f"You have {NR_OF_GUESSES} guesses to get the correct code.")

        # Setup the game
        code = setup_game(NR_OF_COLOURS)

        # Play the game
        play_game(code, NR_OF_GUESSES)

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (Y/n): ")

        if play_again.lower() != "y":
            break


if __name__ == "__main__":
    main()
