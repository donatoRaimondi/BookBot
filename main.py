from stats import get_book_words, get_letter_count, get_report
import sys

def get_book_text(filepath):
    content=""
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py path_to_book")
        sys.exit(1)

    filepath = sys.argv[1]
    print(filepath)
    num_words = get_book_words(get_book_text(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    report = get_report(get_letter_count(get_book_text(filepath)))
    for item in report:
        print(f"{item["char"]}: {item["num"]}" )
    print("============== END ==============")



if __name__ == "__main__":
    main()
