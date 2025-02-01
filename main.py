def main():
    book_path = "books/test.txt"
    word_list = read_book(book_path)
    if word_list:
        print(word_list)
        word_count(word_list)
        characters = character_count(word_list)
        print(f"Number of Characters: {characters}")
        print(character_report(characters))
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
    print(f"Word Count: {len(words.split())}")

#function to return character count
def character_count(words):
    num_char = {}
    working_file = list(words.lower())
    for i in working_file:
        if i in num_char:
            num_char[i] +=1
        else:
            num_char[i] = 1
    return num_char
    
# function to report on character counts, no special characters
def character_report(characters):
    # define allowed characters for report
    allowed_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
    character_dict = {}
    for character in characters:
        if character in allowed_character:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
        elif character not in allowed_character:
            pass
    return character_dict


if __name__ == "__main__":
    main()