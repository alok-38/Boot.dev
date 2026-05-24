import sys
from stats import get_word_count, get_char_count, sort_char_counts


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def main():
    # Must have exactly 2 arguments: script name + file path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    content = get_book_text(file_path)

    number_of_words = get_word_count(content)
    print(f"Found {number_of_words} total words")

    char_counts = get_char_count(content)
    sorted_counts = sort_char_counts(char_counts)

    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()
