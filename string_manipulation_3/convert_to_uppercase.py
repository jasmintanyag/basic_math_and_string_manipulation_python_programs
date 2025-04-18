# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# ask user to input a text/string
# initialize empty string to store the converted result
# create for-loop in every character in text/string
# checks if char is an lowercase letter using ASCII value comparison
# if lowercase, convert to uppercase by subtracting 32 to its ASCII value
# else, if already in uppercase, remain unchanged
# print the uppercase version

text = input("Enter a text: ")
uppercase_result = ""
for char in text:
    if 'a' <= char <= 'z':
        uppercase_result += chr(ord(char) - 32)
    else:
        uppercase_result += char
print("Uppercase version: ", uppercase_result)