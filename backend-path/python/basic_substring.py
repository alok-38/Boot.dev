def basic_substring_extraction(some_string, start, end):
    result = ""
    for index in range(start, end - 1):
        result += some_string[index]
    return result

print(basic_substring_extraction("Alokanana Y", 0,5))
