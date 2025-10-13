import timeit

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = (x for x in numbers if x % 2 == 0)
# print(next(even_numbers))
# print(next(even_numbers))


# using list comprehension
def using_list_comprehension():
    even_numbers = [x for x in numbers if x % 2 == 0]


# using a generator expression
def using_generator_expression():
    even_numbers = (x for x in numbers if x % 2 == 0)


print("Using list comprehension:", timeit.timeit(using_list_comprehension, number=1000))
print(
    "Using generator expression:",
    timeit.timeit(using_generator_expression, number=1000),
)
