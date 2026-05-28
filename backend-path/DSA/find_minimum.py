def find_minimum(numbers: list[int]) -> float | None:
    minimum = float("inf")
    if not numbers:
        return None
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


print(find_minimum([-8, 0, 1, 5]))

