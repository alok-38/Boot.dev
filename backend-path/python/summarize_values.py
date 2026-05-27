def count_basic_types(*values):
    counts = {"int": 0, "str": 0, "bool": 0}

    for value in values:
        if isinstance(value, int) and not isinstance(value, bool):
            counts["int"] += 1
        elif isinstance(value, str):
            counts["str"] += 1
        elif isinstance(value, bool):
            counts["bool"] += 1

    return counts

values = [1, "hi", True, None, 7, False, 3.5]

print(count_basic_types(*values))