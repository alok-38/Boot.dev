def reverse_string(string: str) -> str:
    original_string = string
    empty_string = ""

    for char in original_string:
        empty_string = char + empty_string

    return empty_string

print(reverse_string("Alok"))
