def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    # this function opens and reads the file
    # and returns the contents
        

def get_num_words(book): # your main program logic
    # get_book_text("/home/sufi/workspace/github.com/bootdotdev/bookbot/bookbot/books/frankenstein.txt")
    # this function calls get_book_text - to simplify, it will be universal without any filepath
    # print(get_book_text("/home/sufi/workspace/github.com/bootdotdev/bookbot/bookbot/books/frankenstein.txt"))
    # ^ get the whole book to print out
    words = book.split()
    return len(words)
   
# get_num_words() # This just calls/executes the function, do not need print/return as function already has one.

def get_num_char(book):

    char_count = {}
    lower_charb = book.lower()

    for character in lower_charb:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count

def sort_key(book):
    return book["num"]

def sort_on(book):
    
    char_dict_list = []

    for char, num in book.items():

        if char.isalpha() is True:
            char_dict_list.append({"char": char, "num": num})
        else:
            continue

    char_dict_list.sort(reverse=True,key=sort_key)

    return char_dict_list