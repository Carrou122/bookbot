# from stats import get_num_words

# get_num_words()

#from stats import get_book_text
#from stats import get_num_char
#book = get_book_text("/home/sufi/workspace/github.com/bootdotdev/bookbot/bookbot/books/frankenstein.txt")
#character_count = get_num_char(book)
#print(character_count)

import sys
from stats import get_book_text
from stats import get_num_words
from stats import get_num_char
from stats import sort_on

#while True:
#    filepath = input("Enter the path to the book: ")
#    try:
#        book = get_book_text(filepath)
#        break # Success! Exit the loop.
#    except FileNotFoundError:
#        print("Sorry, that file does not exist.")
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]


book = get_book_text(filepath)    
char_count = get_num_char(book)
word_count = get_num_words(book)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")

for key in sort_on(char_count):
    print(f"{key['char']}: {key['num']}")
print("============= END ===============")