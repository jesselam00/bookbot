import sys
from stats import get_num_words, get_each_char, get_sorted_chars

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"Analyzing book found at {sys.argv[1]}")
    text = get_book_text("./" + sys.argv[1])

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    chars = get_each_char(text)
    sorted_chars = get_sorted_chars(chars)
    for item in sorted_chars:
        print(f"{item["char"]}: {item["num"]}")
    
    print("============= END ===============")

main()