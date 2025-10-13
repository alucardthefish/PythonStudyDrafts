fruits = ["apple", "banana", "cherry"]
quantities = [10, 20, 30]
prices = [0.5, 0.25, 1.0]

print([i for i in zip(fruits, quantities, prices)])

for fruit, qty, price in zip(fruits, quantities, prices):
    total_cost = qty * price
    print(f"{fruit}: {qty} x {price} = ${total_cost}")
