# Lambda (anonymous) functions

# def double(n: int) -> int:
#     return n*2

double = lambda n: n * 2

print(f"{double(10) = }")

larger = lambda a, b: a if a >= b else b


print(f"{larger(10, 48) = }")

names: list[str] = ["Alan", "Gregory", "Zlatan", "Jonas", "Tom", "Augustine"]

names.sort(key=lambda x: len(x))
print(f"{names = }")
