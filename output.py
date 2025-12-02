from stats import get_word_count
from stats import get_char_count

def output_header(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
def output_word_count(path):
    print("------------ Word Count ------------")
    print(f"Found {get_word_count(path)} total words")

def output_char_count(path):
    #chars_dict = {}
    chars_dict = get_char_count(path)
    #chars_dict.sorted(reverse=True, key=str.isalpha)
    #sorted_chars_dict = dict(sorted(chars_dict.items(), reverse=True))
    print("------------ Character Count ------------")
    for key, value in sorted(chars_dict.items(), key=lambda item: item[1], reverse=True):
        if key.isalpha():
            print(f"{key}: {value}")
    #for key, value in sorted_chars_dict:
    #    print(f"{sorted_chars_dict[key][value]}")

def output_footer():
    print("============ END ============")