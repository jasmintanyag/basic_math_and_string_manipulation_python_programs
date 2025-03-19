# Prog08: Create a program that ask the user to input their fullname. Print the number of characters in the input.

# ask user input their full name
name = input("Enter your full name: ")
# print number of characters in input
print(len(name.replace(" ", "")))