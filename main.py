

def read_book(path_to_file):
    try:
        with open(path_to_file, "r") as f:
            file_contents = f.read()
        print(file_contents)
    except:
        print("File Not Found!")

def main():
    read_book("books/frankenstein.txt")

if __name__ == "__main__":
    main()