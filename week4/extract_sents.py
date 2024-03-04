import re
import gzip
import argparse
import os


def tokenizeSentence(line):
    tokens = []
    words = re.split(r'\s', line)
    for token in words:
        tokens += re.split(r'(\,|\!|\?|\"|\&|\;)', token)

    sentence = []
    for token in tokens:
        if len(re.split(r'(^[0-9]+\.[0-9]{2}|^[0-9]+\:[0-9]{2})', token)) > 1:
            sentence.append(token)
            continue
        elif len(re.split(r'(^[A-Z]\.)', token)) > 1:
            sentence.append(token)
            continue
        elif len(re.split(r'(^\w+\-[a-zA-Z]+)', token)) > 1:
            sentence.append(token)
            continue
        elif len(re.split(r'(^[a-zA-Z]+\'s)', token)) > 1:
            sentence.append(token)
            continue
        else:
            sentence += re.split(r'(\.|\:|\-|\')', token)

    tokens = []
    for token in sentence:
        if not token == '':
            tokens.append(token)

    return tokens


def tokenizeLine(filename):
    tokens = []
    count = 0
    with gzip.open(filename, 'rt', encoding='utf8') as inp:
        infile = inp.read()
    p = re.compile(r"""[^ ].*?
                    (?:\.[0-9]+.*?[.!?]\"?|
                    [A-Z]\..*?[A-Z]\..*?[.!?]\"?|
                    [.!?]\"?|
                    \n) """, flags=re.VERBOSE)
    infile = p.findall(infile)
    for line in infile:
        line = line.strip()
        sentence = tokenizeSentence(line)
        # don't print empty lines, don't print until 2 empty lines have passed
        if (not sentence == []) and count >= 2:
            tokens.append(sentence)
            print(' '.join(sentence))
        else:
            # count the first 2 empty lines, after this the article starts
            count += 1
    return tokens


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

    # call on function to tokenize the file
    tokens = tokenizeLine(args.input)


if __name__ == '__main__':
    main()
