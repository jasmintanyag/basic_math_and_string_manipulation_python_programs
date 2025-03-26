# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# ask user to input their full name in incorrect casing
# print each character input in reverse casing

name = input("Enter your full name in incorrect casing: ")
print("Reversed case: ", name.swapcase())