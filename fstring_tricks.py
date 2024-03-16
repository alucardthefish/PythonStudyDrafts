from datetime import datetime, date


# Trick 1
n: int = 1_000_000_000

print(f"{n:_}")  # will print 1_000_000_000
print(f"{n:,}")  # will print 1,000,000,000


# Trick 2
var: str = "var"

print(f"{var:_>20}:")
print(f"{var:#<20}:")
print(f"{var:|^20}:")
print(f"{'':!>20}")

# Trick 3

now: datetime = datetime.now()
print(f"{now:%d.%m.%y}")
print(f"{now:%c}")


# Trick 4

n: float = 1234.5678
print(f"{n:.2f}")
print(f"{n:.0f}")
print(f"{n:,.3f}")


# Trick 5

a: int = 5
b: int = 10
my_var: str = "Bob says hi"

print(f"{my_var = }")
print(f"{a + b = }")


# Trick 6 Scientific notation

big_number: int = 1_620_000_000

print(f"{big_number:e}")  # 1.620000e+09
print(f"{big_number:.2e}")  # 1.62e+09


# Trick 7

date_spec: str = "%d.%m.%Y"
print(f"{now:{date_spec}}")

num: float = 1000000.1234567
spec: str = ",.2f"
print(f"{num:{spec}}")


# Trick 8

custom_folder: str = "my_folder"
path: str = fr"\Users\fico\documents\{custom_folder}"
print(path)


# Trick 9

a: float = 0.1
b: float = 0.2

print(f"{a + b = :.1f}")


# Trick 10

banana: str = "🍌"
name: str = "Bob"
today: date = datetime.now().date()

print(f"[{today!s}] {name!s} says: {banana!s}")
print(f"[{today!r}] {name!r} says: {banana!r}")
print(f"[{today!a}] {name!a} says: {banana!a}")
