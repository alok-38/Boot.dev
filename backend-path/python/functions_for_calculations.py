def price_calculation(cost_price, overhead_cost, markup, demand_factor, discount, shipping, tax):
    price = (
        (cost_price + overhead_cost)
        * (1 + markup)
        * demand_factor
        * (1 - discount)
        + shipping
        + tax
    )
    return price

price = price_calculation(
    cost_price=100,
    overhead_cost=20,
    markup=0.3,
    demand_factor=1.1,
    discount=0.1,
    shipping=5,
    tax=10
)

print(price)
