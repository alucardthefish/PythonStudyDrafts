import math


numbers: list[int] = [49, 64, 81, 100, 121]

new_list: list[int] = [int(math.sqrt(n)) for n in numbers if n % 2 == 0]

print(f"{new_list = }")

team_1: list[str] = ["Janet", "Arya", "Mary"]
team_2: list[str] = ["Evan", "Jake", "Randy"]

new_teams: list[tuple] = [(x, y) for x in team_1 for y in team_2]

print(f"{new_teams = }")

# square_dict = dict()
#
# for num in numbers:
#     square_dict[num] = num**2

square_dict: dict = {num: num**2 for num in numbers}

print(f"{square_dict = }")

old_price: dict = {"milk": 1.02, "coffe": 2.5, "bread": 2.5}

new_price: dict = {
    key: value * 1.5 if value > 2 else value for (key, value) in old_price.items()
}

print(f"{new_price = }")
