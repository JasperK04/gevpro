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


def main():

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
