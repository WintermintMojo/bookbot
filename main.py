def main():
    with open("books/frankenstein.txt") as book:
        file_contents = book.read()
    print(file_contents)
    print(len(file_contents.split()))

if __name__ == '__main__':
    main()