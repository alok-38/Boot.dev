def find_top_word(words):
    word_freq = {}

    # Step 1: Count frequencies
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Step 2: Find max
    max_word = None
    max_count = 0

    for word, count in word_freq.items():
        if count > max_count:
            max_word = word
            max_count = count

    return max_word, max_count

words = ["a", "b", "a", "c", "a", "b"]
print(find_top_word(words))


