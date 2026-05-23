from stats import get_word_count, get_char_count

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

def main():
    file_path = "books/frankenstein.txt"
    content = get_book_text(file_path)

    number_of_words = get_word_count(content)
    print(f"Found {number_of_words} total words")

    # NEW: get character counts
    char_counts = get_char_count(content)

    # Print the dictionary
    print(char_counts)

if __name__ == "__main__":
    main()
