def get_book_text(path):
    # Opening file and returning its contents.
    with open(path, 'r', encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents
    
def get_word_count(book):
    # takes in a book and returns the number of words in the book.
    words = []
    book_text = get_book_text(book)
    words = book_text.split()
    return len(words)

def get_char_count(book):
    # get the book contenst as a string and return the count of each char as a dict.
    char = ""
    book_text = get_book_text(book)
    chars_dict = {}
    for char in book_text:
        # if the char is already in the dict add one to the value. else creates new dict entry with value 1.
        if char.lower() in chars_dict and isinstance(chars_dict[char.lower()], (int, float)):
            chars_dict[char.lower()] += 1
        else:
            new_entry = {char.lower() : 1}
            chars_dict.update(new_entry)
    return chars_dict