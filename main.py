from stats import count_words
from stats import char_count
from stats import sorted_dictionaries_list


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
    


main ("books/frankenstein.txt")