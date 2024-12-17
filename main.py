def main():
    filePath = "books/frankenstein.txt"
    book_content= read_book(filePath)
    wordCount = count_words(book_content)
    charDict = count_characters(book_content)
    output_report(filePath,wordCount,charDict)

def read_book(path):
    with open(path) as book:
        file_contents = book.read()
    return file_contents

def count_words(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):
    words = text.split()
    unique_chars = {}
    for word in words:
        for char in word:
            if char.lower() in unique_chars and char.isalpha():
                unique_chars[char.lower()] = unique_chars[char.lower()] + 1
            elif char.isalpha():
                unique_chars[char.lower()] = 1
    return unique_chars

def output_report(path,words,charDict):
    print(f'--- Begin report of {path} ---')
    print(f'{words} words found in the document')

    for entry in charDict:
        print(f"The '{entry}' character was found {charDict[entry]} times")
    print(f'--- End Report ---')


if __name__ == '__main__':
    main()