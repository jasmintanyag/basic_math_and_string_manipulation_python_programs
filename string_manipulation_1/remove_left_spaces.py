# Prog01: Create a program that ask the user to input their full name with several space characters at the beginning. Print the input without the spaces in the beginning.

# ask user to input their full name with several spaces at the beginning
# remove the spaces in the beginning using the left strip method
# print the input without spaces at beginning

name = input("Enter your full name (add space/s at the beginning): ").lstrip()
print("Your name is: ", name)