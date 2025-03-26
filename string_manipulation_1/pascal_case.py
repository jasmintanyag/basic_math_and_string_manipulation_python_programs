# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# ask user input their name in incorrect casing
# print input in pascal case

name = input("Enter your full name in incorrect casing: ")
print("Name in Pascal Case: ", name.title().replace(" ", ""))