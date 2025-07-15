from stats import count_words
from stats import char_count

def main(path):
    print (count_words(path), char_count(path))
    return (count_words(path), char_count(path))

main ("books/frankenstein.txt")