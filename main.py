def main():
    book_path = "books/frankenstein.txt"
    word_list = read_book(book_path)
    word_count(word_list)

    

''' main with input option
def main():
    file_path = f"books/{input('Enter the file name: ')}"
    read_book(file_path)
'''

#function to read file and print to stdout
def read_book(path_to_file):
    try:
        with open(path_to_file, "r") as f:
            file_contents = f.read()
            print(file_contents)
        return file_contents
    except:
        print("File Not Found!")
    
#function to return word count
def word_count(word_list):
    try:
        words = len(word_list.split())
        print(f"Word Count: {words}")
    except:
        print("File Not Found, Cannot Count Words!")

if __name__ == "__main__":
    main()