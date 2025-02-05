def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents
    
def count_words(foo):
    words = foo.split()
    word_count = len(words)
    return word_count

def count_characters(bar):
    char_dict = {}
    to_lower_case = bar.lower()
    for char in to_lower_case:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1      
    return char_dict

whole_book = main()
word_count = count_words(whole_book)
character_count = count_characters(whole_book)
print(character_count)