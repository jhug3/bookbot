import sys

from output import *


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    output_header(path)
    output_word_count(path)
    output_char_count(path)
    output_footer()
    #char_count = get_char_count("books/frankenstein.txt")
    #print(char_count)

# calling main
main()
    

