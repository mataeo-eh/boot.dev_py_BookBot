

def count_words(path):
    text= get_book_text(path)
    word_count= text.split() 
    final_count = len(word_count)
    # return f"{final_count} words found in the document"
    # print (final_count)
    return final_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)

def char_count(path):
    text= get_book_text(path).lower()
    characters_dictionary = {}
    for character in text:
        if character not in characters_dictionary:
            characters_dictionary[character] = 1 
        else:
            characters_dictionary[character] += 1
    return characters_dictionary

def sorting_key(to_sort):
    return to_sort["num"]


def sorted_dictionaries_list(path):
    dictionary = char_count(path)
    new_dics_list = []
    analyzed_count = []
    for character in dictionary:
        number = dictionary[character]
        if character.isalpha() == True:
            new_dics_list.append({"char": character, "num": number})
            new_dics_list.sort(reverse=True, key=sorting_key)
    # Below used for testing purposes
    # print (new_dics_list)
    # return new_dics_list[1]["char"], new_dics_list[1]["num"]
    # for dictionary in new_dics_list:
        #analyzed_count.append(f"{dictionary["char"]}: {dictionary["num"]}")
    # analyzed_count_string = " ".join(analyzed_count)
       # print (f"{dictionary["char"]}: {dictionary["num"]}")
    return new_dics_list
    


# used for testing, kept to use as a reference.
# ef main (path):
   # print (sorted_dictionaries_list(path))
   # print (char_count(path))
   # print (sorted_dictionaries_list(path)) 



# See above.
# main("books/frankenstein.txt")