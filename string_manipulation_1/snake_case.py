# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# ask user input their name in incorrect casing
# print input in snake case

name = input("Enter your full name in incorrect casing: ")
print("Name in Snake Case: ", name.lower().replace(" ", "_"))