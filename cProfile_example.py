import cProfile

"""
cProfile helps to find which part of the program or code takes more time to run

Interesting info here: https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_prime():
    for i in range(1, 1000):
        is_prime(i)


def print_primes_until_n(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print(f"Prime: {i}")


cProfile.run("test_prime()")
# print(is_prime(11))
# print_primes_until_n(1000)


def prime_997():
    is_prime(997)


cProfile.run("prime_997()")
