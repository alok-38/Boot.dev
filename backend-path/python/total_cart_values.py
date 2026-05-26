def add_value(total, value):
    return total + value


def total_cart_values(values):
    total = 0
    for value in values:
        total = add_value(total, value)
    return total