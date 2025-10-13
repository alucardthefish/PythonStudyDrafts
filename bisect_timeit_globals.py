import timeit
from bisect import bisect_left

sequence = list(range(0, 10000, 2))
# print(sequence)


def find_closest_brute_force(sequence, goal):
    for index, value in enumerate(sequence):
        if goal <= value:
            return index


def find_closest_bisect(sequence, goal):
    index = bisect_left(sequence, goal)
    return index


brute_force_time = timeit.timeit(
    stmt="find_closest_brute_force(sequence, 9500)", globals=globals(), number=1000
)

# print("globals: ", globals())


binary_time = timeit.timeit(
    stmt="find_closest_bisect(sequence, 9500)", globals=globals(), number=1000
)

print(f"Time for brute force {brute_force_time}")
print(f"Time for bisect method {binary_time}")

print(
    "find_closest_brute_force(sequence, 9500): ",
    find_closest_brute_force(sequence, 9500),
)
print("find_closest_bisect(sequence, 9500): ", find_closest_bisect(sequence, 9500))
