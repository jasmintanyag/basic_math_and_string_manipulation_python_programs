# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# ask user to input a text/string
# initialize empty string to store the converted result
# create for-loop in every character in text/string
# checks if char is an uppercase letter using ASCII value comparison
# if uppercase, convert to lowercase by adding 32 to its ASCII value
# else, if already in lowercase, remain unchanged
# print the lowercase version

text = input("Enter a text: ")
lowercase_result = ""
for char in text:
    if 'A' <= char <= 'Z':
        lowercase_result += chr(ord(char) + 32)
    else:
        lowercase_result += char
print("Lowercase version: ", lowercase_result)