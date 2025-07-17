from stats import count_words
from stats import char_count
from stats import sorted_dictionaries_list
import sys


#def generic_use():



def main(path):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}")
    print ("----------- Word Count ----------")
    print (f"Found {count_words(path)} total words")
    print ("--------- Character Count -------")
    for char_dict in sorted_dictionaries_list(path):
        print (f"{char_dict["char"]}: {char_dict["num"]}")
    print ("============= END ===============")

    return 
    
if len(sys.argv) <= 1:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]
    print (main(path))

# main ("books/frankenstein.txt") #Made a comment just for testing purposes