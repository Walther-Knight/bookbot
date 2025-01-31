

def main():
    path_to_file = "books/frankenstein.txt"
    try:
        with open(path_to_file, "r") as f:
            file_contents = f.read()
        print(file_contents)
    except:
        print("File Not Found!")

main()