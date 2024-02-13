import xml.etree.ElementTree as ET
import sys


def get_adjectives(filename: str = "cdb-sample.xml") -> set:
    adjectives = set()
    tree = ET.parse(filename)
    cdbid = tree.getroot()
    for cid in cdbid:
        pos = cid.attrib["pos"]
        if pos == "ADJ" and cid.attrib["form"] != "":
            adjectives.add(cid.attrib["form"])

    return adjectives


def main():
    if len(sys.argv) > 1:
        adj = sorted(get_adjectives(sys.argv[1]))
        for word in adj:
            print(word)
    else:
        adj = get_adjectives()
        print(adj)


if __name__ == "__main__":
    main()
