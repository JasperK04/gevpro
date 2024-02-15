import xml.etree.ElementTree as ET
import argparse as ap
import time
import os


def get_adjectives(filename: str = "cdb-sample.xml") -> set:
    """
    this function finds all adjectives in the specified xml file.
    It then output a set the set of words that are adjectives.
    """
    adjectives = set()
    tree = ET.parse(filename)
    cdbid = tree.getroot()
    for cid in cdbid:
        pos = cid.attrib["pos"]
        if pos == "ADJ" and cid.attrib["form"] != "":
            adjectives.add(cid.attrib["form"])

    return adjectives


def input_tests(args):
    # test first argument
    if args.lex is not None:
        if not isinstance(args.lex, str):
            print("argument <file> is not a string")
            exit(-1)
        if args.lex[-4:] != ".xml":
            print("argument <file> is not of file type xml")
            exit(-1)
        if not os.path.exists(args.lex):
            print(f"{args.lex} does not exist in directory")
            exit(-1)


def create_parser():
    # create the command line argument parser
    parser = ap.ArgumentParser(description="finds adjectives")
    parser.add_argument("lex", metavar="<lexicon>", type=str, nargs="?",
                        help="Optionally add lexicon to find the adjectives in\
                            (default is 'cdb-sample.xml')")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enables the debug mode")
    return parser.parse_args()


def main():

    # create the command line argument parser
    args = create_parser()

    # test if the argument is valid (if there is any)
    input_tests(args)

    # check if the debug flag is set
    if args.debug:
        start = time.perf_counter()

    # call the correct version of the get_adjectives function
    if args.lex is not None:
        adj = sorted(get_adjectives(args.lex))
        for word in adj:
            print(word)
    else:
        adj = get_adjectives()
        print(adj)

    # check if debug flag is set and print extra information
    if args.debug:
        end = time.perf_counter()
        print(f"parameter value of 'get_adjective' is: '{args.lex}'")
        print(f"length of resulting set is: {len(adj)}")
        print(f"time to execute 'get_adjectives': {end - start} seconds")


if __name__ == "__main__":
    main()
