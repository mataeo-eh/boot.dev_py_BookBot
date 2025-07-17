from stats import count_words
from stats import char_count
from stats import sorted_dictionaries_list
import sys

def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}")
    print ("----------- Word Count ----------")
    print (f"Found {count_words(path)} total words")
    print ("--------- Character Count -------")
    for char_dict in sorted_dictionaries_list(path):
        print (f"{char_dict['char']}: {char_dict['num']}")
    print ("============= END ===============")
    return 


if __name__ == "__main__":
    try:
        main()
    except Exception as input_error:
        print (input_error)
        sys.exit(1)