# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# ask user to input a string
# ask again to input a substring to count
# initialize a counter
# loop through string and count its occurences
# check if substring matches, add 1 to count if matched
# print the result

text = input("Enter a text: ")
substring = input("Enter the substring to count: ")
counts = 0

for i in range(len(text) - len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        counts += 1

print(f"'{substring}' appeared {counts} time(s)")