from random import choice, choices
from collections import defaultdict
import argparse

# Set to True to enable debug mode
DEBUG = False

# Game settings
NR_OF_GUESSES = 8
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


def simulate_game(code: list[str], length: int = 4):
    '''
    This function will simulate the game and return True if the player wins.
    '''
    options = ["red", "green", "blue", "yellow", "purple", "orange"]

    option_list = [options[:] for _ in range(length)]

    for attemts in range(NR_OF_GUESSES):

        guess = []
        for i in range(length):
            guess.append(choice(option_list[i]))
        
        colours_in_code = {colour: code.count(colour) for colour in options}

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
                result[i] = "misplaced"

        if correct == length:
            #print('correct')
            return True, attemts + 1

        skip = []
        for i in range(len(code)):
            status = tuple([result[i], guess[i], i])
            if result[i] == 'not included':
                delete = guess[i]
                if guess[i] not in skip:
                    for j in range(len(option_list)):
                        if guess[i] in option_list[j] and len(option_list[j]) > 1:
                            option_list[j].remove(guess[i])
                else:
                    option_list[i].remove(guess[i])

            if result[i] == 'correct':
                option_list[i] = [guess[i]]

            if result[i] == 'misplaced':
                option_list[i].remove(guess[i])
                skip.append(guess[i])
        
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
    parser.add_argument("simulate", metavar='simulate n times', nargs=1, type=int,
                        help="Simulate the game the specified number of times.")
    return parser.parse_args()


def main():

    args = create_parser()

    simulate_n_iterations(args.simulate[0])


if __name__ == "__main__":
    main()
