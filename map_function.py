# Map function example

numbers = [1, 2, 3, 4, 5]

squared_nums = map(lambda n: n**2, numbers)

squared_nums = list(squared_nums)

print(f"{squared_nums = }")

num_1 = [4, 5, 6]
num_2 = [5, 6, 7]

result = list(map(lambda n1, n2 : n1 + n2, num_1, num_2))

print(f"{result = }")
