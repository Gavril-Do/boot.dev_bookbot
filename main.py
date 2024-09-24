def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_char(text)
    num_characters = dic_sort(num_characters)
    print(num_characters)

def get_num_words(string):
    words = string.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(string):
    characters = {}
    string_lower = string.lower()
    for c in string_lower:
        characters[c] = characters.get(c, 0) + 1
    #    print(characters)
    return characters

def dic_sort(dic):
    keys = list(dic.keys())
    keys.sort()
    dic = {i: dic[i] for i in keys}
    return dic

main()