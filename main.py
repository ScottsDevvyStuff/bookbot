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

def sort_on(dict):
    return dict["count"]

def sort_and_report(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():  # Only include alphabet characters
            char_list.append({"character": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for char in char_list:
        print(f"The {char} character was found {count} times")
    print("--- End report ---")

whole_book = main()
word_count = count_words(whole_book)
character_count = count_characters(whole_book)
report = sort_and_report(character_count)