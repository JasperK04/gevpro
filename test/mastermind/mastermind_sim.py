from random import choice, choices
from collections import defaultdict
import argparse

# Set to True to enable time tracking
TIME = False
if TIME:
    import time

# Set to True to enable debug mode
DEBUG = False

# Game settings
NR_OF_GUESSES = 6
NR_OF_COLOURS = 4


def setup_game(nr_of_colours: int = 4) -> list[str]:
    '''
    This function will setup the game by generating a random code for the player to guess.
    '''
    colours = [1, 2, 3, 4, 5, 6]
    code = choices(colours, k=nr_of_colours)

    if DEBUG:
        code = [1, 2, 3, 4]
        print(f"DEBUG: The code is {code}")

    return code


def simulate_game(code: list[str], length: int = 4):
    '''
    This function will simulate the game and return True if the player wins.
    '''
    options = [1, 2, 3, 4, 5, 6]

    option_list = [options[:] for _ in range(length)]

    for attemts in range(NR_OF_GUESSES):

        guess = []
        for i in range(length):
            guess.append(choice(option_list[i]))
        
        colours_in_code = {colour: code.count(colour) for colour in options}

        correct = 0
        skip = []

        for i in range(len(code)):
            guess_color = guess[i]
            code_color = code[i]

            if guess_color == code_color:
                correct += 1
                colours_in_code[guess_color] -= 1
                # only one option left
                option_list[i] = [guess[i]]

                if correct == length:
                    return True, attemts + 1

            elif colours_in_code[guess_color] > 0 and guess_color != code_color:
                colours_in_code[guess_color] -= 1
                # remove the option from the list
                option_list[i].remove(guess[i])
                skip.append(guess[i])

            else:
                if guess[i] not in skip:
                    for j in range(len(option_list)):
                        if guess[i] in option_list[j] and len(option_list[j]) > 1:
                            option_list[j].remove(guess[i])
                else:
                    option_list[i].remove(guess[i])

    return False, 'unsolved'
    

def simulate_n_iterations(iterations: int = 1000):
    '''
    This function will simulate the game n times and return the percentage of wins.
    '''
    if TIME:
        start_time = time.time()

    # Simulate the game and count the wins
    wins = 0
    total_nr_of_guesses = defaultdict(int)
    for _ in range(iterations):
        code = setup_game(NR_OF_COLOURS)
        solved, attemts = simulate_game(code, NR_OF_COLOURS)
        total_nr_of_guesses[attemts] += 1
        if solved:
            wins += 1

    if TIME:
        end_time = time.time()
        print(f"Simulation took {end_time - start_time:.2f} seconds.")
    
    # Print the results
    persentage = wins / iterations * 100
    print(f"Out of {iterations} games, the player won {wins} times ({persentage:.2f}%).")
    for i in range(1, NR_OF_GUESSES + 1):
        print(f"{i} guesses: {total_nr_of_guesses[i]} times.")
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
