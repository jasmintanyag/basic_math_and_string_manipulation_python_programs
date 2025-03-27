# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# ask user to input a text/string
text = input("Enter a text: ")
# initialize empty string to store the converted result
lowercase_result = ""
# create for-loop in every character in text/string
for char in text:
# checks if char is an uppercase letter using ASCII value comparison
    if 'A' <= char <= 'Z':
# if uppercase, convert to lowercase by adding 32 to its ASCII value
        lowercase_result += chr(ord(char) + 32)
# else, if already in lowercase, remain unchanged
    else:
        lowercase_result += char
# print the lowercase version