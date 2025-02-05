def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents
    
def count_words(foo):
    words = foo.split()
    word_count = len(words)
    return word_count

whole_book = main()
word_count = count_words(whole_book)
print(word_count)