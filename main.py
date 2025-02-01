def main():
    book_path = "books/frankenstein.txt"
    word_list = read_book(book_path)
    if word_list:
        print(word_list)
        number_of_words = word_count(word_list)
        characters = character_count(word_list)
        character_report(characters, book_path, number_of_words)
        
    else:
        print("File Not Found!")
    
    

''' main with input option
def main():
    file_path = f"books/{input('Enter the file name: ')}"
    read_book(file_path)
'''

#function to read file and print to stdout
def read_book(path_to_file):
    try:
        with open(path_to_file, "r") as f:
            return f.read()
    except:
        return None
    
#function to return word count
def word_count(words):
    return len(words.split())

#function to return character count
def character_count(words):
    # define allowed characters for report
    allowed_character = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",}
    num_char = {}
    working_file = list(words.lower())
    for i in working_file:
        if i in allowed_character:
            if i in num_char:
                num_char[i] +=1
            else:
                num_char[i] = 1
    return num_char
    
# function to report on character counts, no special characters
def character_report(characters, book_path, number_of_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print("")
    for character in characters:
        print(f"The '{character}' character was found {characters[character]} times")
    print("--- End Report ---")


if __name__ == "__main__":
    main()