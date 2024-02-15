import json
import os
import time
import tracemalloc as tr
from collections import defaultdict
import argparse


def find_many(query: str, filename: str) -> dict:
    """
    this function finds all anagrams for each word in a query input file.
    it finds its anagrams in a specified json file.
    Then it outputs a dictionary of words that are anagrams.
    the keys in this dictionary are the query words sorted alphabetically.
    """
    data = defaultdict(list)
    with open(query, "r") as inp:
        for word in inp:
            word = word.lower().strip()
            sorted_word = "".join(sorted(word))
            data[sorted_word].append(word)

    with open(filename, "r") as inp:
        file = set(json.load(inp)['words']['dutch'])
        for word in file:
            word = word.lower().strip()
            sorted_word = "".join(sorted(word))
            if sorted_word in data.keys():
                data[sorted_word].append(word)

    return data


def find(word: str, filename: str = "words.json") -> set:
    """
    this function finds anagrams of the specified word in a json file.
    It then output a set of words that are anagrams of the specified word
    """
    # Convert word to lowercase and sort its characters
    sorted_word = sorted(word.lower())
    anagramSet = set()

    # Open the file
    with open(filename, 'r') as inp:
        data = set(json.load(inp)['words']['dutch'])
        # Iterate through each line in the file
        for w in data:
            # Convert word to lowercase and sort its characters
            sorted_w = sorted(w.lower())
            # check if the sorted characters match, it's an anagram
            if sorted_w == sorted_word:
                anagramSet.add(w)

    return anagramSet


def input_tests(args):
    # test first argument
    if not isinstance(args.word, str):
        print("argument <word> is not a string")
        exit(-1)

    # test second argument
    if not isinstance(args.file, str):
        print("argument <file> is not a string")
        exit(-1)
    if args.file[-5:] != ".json":
        print("argument <file> is not of file type json")
        exit(-1)
    if not os.path.exists(args.file):
        print(f"{args.file} does not exist in directory")
        exit(-1)

    # test third argument
    if not isinstance(args.query, str):
        print("argument <query> is not a string")
        exit(-1)
    if args.query[-4:] != ".txt":
        print("argument <query> is not of file type txt")
        exit(-1)
    if not os.path.exists(args.query):
        print(f"{args.query} does not exist in directory")
        exit(-1)


def create_parser():
    # create the command line argument parser
    parser = argparse.ArgumentParser(description="finds anagrams")
    parser.add_argument("word", metavar="<word>", type=str, default="eten",
                        help="Enter a word to find the anagrams of")
    parser.add_argument("file", metavar="<file.json>", type=str, nargs="?",
                        default="words.json",
                        help="Optionally supply a json source")
    parser.add_argument("query", metavar="<query.txt>", type=str, nargs="?",
                        default="query.txt",
                        help="Optionally add a query for 'find_many'")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enables the debug mode")
    parser.add_argument("-t", "--time", action="store_true",
                        help="Enables the timed results")
    parser.add_argument("-o", "--one", action="store_true",
                        help="use only the 'find' function")
    parser.add_argument("-m", "--many", action="store_true",
                        help="use only the 'find_many' function")
    return parser.parse_args()


def main():
    # create the command line argument parser
    args = create_parser()

    # call on function to test if input is valid
    input_tests(args)

    # check if debug or time flag has been set
    if args.debug or args.time:
        start = start2 = time.perf_counter()

    # find #
    # check if function 'find' has to be called
    if not args.many:
        word = args.word
        filename = args.file
        anagramSet = find(word, filename)

        # check if debug flag has been set
        if args.debug:
            end = time.perf_counter()
            print(f"parameter values of 'find' are: '{word}' and '{filename}'")
            print(f"length of resulting set is: {len(anagramSet)}")
            print(f"time to execute 'find': {end - start} seconds")
            start = end
        else:
            # print the output of the find function
            print(f"Anagrams of '{word}' in '{filename}': \n{anagramSet}")

            # check if flag for time is set
            if args.time:
                end = time.perf_counter()
                print(f"time to execute 'find': {end - start} seconds")
                start = end

    # find_many #
    # check if function 'find_many' has to be called
    if not args.one:
        filename = args.file
        query = args.query
        anagramDict = find_many(query, filename)

        #  check if debug flag has been set
        if args.debug:
            end = time.perf_counter()
            print(f"parameter values of 'find_many' are: "
                  f"'{query}' and '{filename}'")
            print(f"length of resulting dictionary is: {len(anagramDict)}")
            print(f"time to execute 'find many': {end - start} seconds")
        else:
            # print the output of the 'find_many' function
            for key in anagramDict.keys():
                print(f"Anagrams of {anagramDict[key][0]} are: ", end="")
                print(f"{set(anagramDict[key])}")

            # check if flag for time is set
            if args.time:
                end = time.perf_counter()
                print(f"time to execute 'find_many': {end - start} seconds")

    # check if flag for debug or time is set and not already displayed
    if (args.debug or args.time) and not (args.one or args.many):
        end = time.perf_counter()
        print(f"total time to execute: {end - start2} seconds\n")


if __name__ == "__main__":
    main()
