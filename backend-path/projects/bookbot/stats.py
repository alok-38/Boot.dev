def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

def get_char_count(text: str) -> dict:
    char_count = {}

    for char in text:
        char = char.lower()  # normalize to lowercase

        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1

    return char_count
