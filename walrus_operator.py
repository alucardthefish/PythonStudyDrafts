# What is the walrus operator: walrus operator is available for Python 3.8 or greater
# Walrus known as --> :=


user_input = input("Enter a word (or 'quit' to exit): ")
while user_input != "quit":
    print(f"You entered the word: {user_input}")
    user_input = user_input = input("Enter a word (or 'quit' to exit): ")

while (user_input := input("Enter a word (or 'quit' to exit): ")) != "quit":
    print(f"You entered the word: {user_input}")

(user_input := input("Enter a word (or 'quit' to exit): "))
print("user_input: ", user_input)
