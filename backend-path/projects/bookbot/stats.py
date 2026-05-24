from typing import TypedDict


class CharacterCount(TypedDict):
    char: str
    num: int


def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict[str, int]:
    char_count: dict[str, int] = {}

    for char in text:
        if not char.isalpha():
            continue

        char = char.lower()

        char_count[char] = char_count.get(char, 0) + 1

    return char_count


def sort_char_counts(char_counts: dict[str, int]) -> list[CharacterCount]:
    result: list[CharacterCount] = []

    for char, num in char_counts.items():
        result.append({"char": char, "num": num})

    def sort_on(item: CharacterCount) -> int:
        return item["num"]

    result.sort(key=sort_on, reverse=True)

    return result
