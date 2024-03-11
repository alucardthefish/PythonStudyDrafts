# Filter function example

numbers = [234, 3245, 639, 550, 654, 4432, 537, 457, 789, 12345, 6848]

even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print(f"{even_numbers = }")
