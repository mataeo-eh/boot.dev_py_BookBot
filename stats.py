def count_words(path):
    text= get_book_text(path)
    word_count= text.split() 
    final_count = len(word_count)
    return f"{final_count} words found in the document"
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    number = count_words("books/frankenstein.txt")
    print (number)
    

main()