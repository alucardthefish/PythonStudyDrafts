a = [1, 2, 3, 4, 5]
b = a

# Change the 4th index in b
b[4] = 7

print(id(a))
print(id(b))
print(a)  # Remember we did not explicitly make changes to a.

b = a[:]  # Creating a clone of the list a. Another ways of cloning below
# c = list(a)
# d = a.copy()

print("list a: ", a)
print("list b: ", b)
b[2] = 100

print("list b after change: ", b)
print("list a after b changes: ", a)
