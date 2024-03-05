import re
import gzip
import argparse
import os


def tokenizeToWords(line):
    """
    This function takes a line and returns a list of tokens
    Each token is either a punctuation, a word or a number.
    """
    # split the sentence into tokens at spaces and non special punctuation
    tokens = []
    words = re.split(r'\s', line)
    for token in words:
        tokens += re.split(r'(\,|\!|\?|\"|\&|\;)', token)

    # for each token check if a special case applies
    # if not so just add the word to the sentence list
    sentence = []
    for token in tokens:
        if len(re.split(r'(^[0-9]+\.[0-9]{2}|^[0-9]+\:[0-9]{2})', token)) > 1:
            # check if the token is a number with a '.' or ':' in between
            sentence.append(token)
        elif len(re.split(r'(^[A-Z]\.)', token)) > 1:
            # check if the token is a capitalized letter followed by a '.'
            sentence.append(token)
        elif len(re.split(r'(^\w+\-[a-zA-Z]+)', token)) > 1:
            # check if the token is two words with a '-' in between
            sentence.append(token)
        elif len(re.split(r'(^[a-zA-Z]+\'s)', token)) > 1:
            # check if the token is a word ending with "'s"
            sentence.append(token)
        else:
            sentence += re.split(r'(\.|\:|\-|\')', token)

    # re.split creates empty str in beween of punctuation
    # remove those empty strings again from the sentence
    tokens = []
    for token in sentence:
        if not token == '':
            tokens.append(token)

    return tokens


def tokenizeToLines(filename):
    """
    This function takes an input file and creates a list of tokens
    Each token is a centense.
    """
    # keep a counter that counts the number of white lines printed
    count = 0
    # open the file
    with gzip.open(filename, 'rt', encoding='utf8') as inp:
        infile = inp.read()
    # compile the line splitter
    p = re.compile(r"""[^ ].*?
                    (?:\.[0-9]+.*?[.!?]\"?|
                    [A-Z]\..*?[A-Z]\..*?[.!?]\"?|
                    [.!?]\"?|
                    \n) """, flags=re.VERBOSE)
    infile = p.findall(infile)
    # for each line in the infile call the tokenizer and print the result
    for line in infile:
        line = line.strip()
        sentence = tokenizeToWords(line)
        # don't print empty lines, don't print until 2 empty lines have passed
        if (not sentence == []) and count >= 2:
            print(' '.join(sentence))
        else:
            # count the first 2 empty lines, after this the article starts
            count += 1


def input_tests(args):
    # test first argument
    if not isinstance(args.input, str):
        print("argument <input file> is not a string")
        exit(-1)
    if not args.input[-3:] == ".gz":
        print("argument <input file> is not of file type 'gz'")
        exit(-1)
    if not os.path.exists(args.input):
        print(f"{args.input} does not exist in directory")
        exit(-1)


def create_parser():
    # create the command line argument parser
    parser = argparse.ArgumentParser(description="create tokenized file")
    parser.add_argument("input", metavar="<input file>", type=str,
                        help="Enter a valid .gz file to tokenize")
    return parser.parse_args()


def main():
    # create the command line argument parser
    args = create_parser()

    # call on function to test if input is valid
    input_tests(args)

    # call on function to tokenize and print the output
    tokenizeToLines(args.input)


if __name__ == '__main__':
    main()
