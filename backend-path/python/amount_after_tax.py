def calculate_total_with_tax(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate / 100
    return subtotal + tax

prices = [100, 200, 50]
tax_rate = 10

print(calculate_total_with_tax(prices, tax_rate))
