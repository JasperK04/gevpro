import json
import time
from collections import defaultdict
import argparse


def find_many(query: str = "query.txt", filename: str = "words.json"):
    data = defaultdict(list)
    with open(query, "r") as inp:
        for word in inp:
            word = word.lower().strip()
            sorted_word = "".join(sorted(word))
            data[sorted_word].append(word)

    with open(filename, "r") as inp:
        file = set(json.load(inp)['words']['dutch'])
        for word in file:
            sorted_word = "".join(sorted(word.lower().strip()))
            if sorted_word in data.keys():
                data[sorted_word].append(word)

    for key in data.keys():
        print(f"Anagrams of {data[key][0]} are: {set(data[key])}")

    return data


def find(word: str, filename: str = "words.json") -> set:
    """
    this method finds anagrams of the specified word in a json file.
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


def main():
    parser = argparse.ArgumentParser(description="finds anagrams")
    parser.add_argument("word", metavar="<word>", type=str,
                        help="Enter a word to find the anagrams of")
    parser.add_argument("file", metavar="<file.json>", type=str, nargs="?",
                        default="words.json", help="Optionally add a source")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enables debug mode")
    args = parser.parse_args()
    if args.debug:
        start = time.perf_counter()

    word = args.word
    filename = args.file
    anagramSet = find(word, filename)
    print(f"Anagrams of '{word}' in '{filename}': \n{anagramSet}")

    anagramDict = find_many("query.txt", filename)
    for key in anagramDict.keys():
        print(f"Anagrams of {anagramDict[key][0]} are:\
               {set(anagramDict[key])}")

    if args.debug:
        end = time.perf_counter()
        print(end - start)


if __name__ == "__main__":
    main()
