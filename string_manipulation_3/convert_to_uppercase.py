# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# ask user to input a text/string
text = input("Enter a text: ")
# initialize empty string to store the converted result
uppercase_result = ""
# create for-loop in every character in text/string
for char in text:
# checks if char is an lowercase letter using ASCII value comparison
    if 'a' <= char <= 'z':
# if lowercase, convert to uppercase by subtracting 32 to its ASCII value
        uppercase_result += chr(ord(char) - 32)
# else, if already in uppercase, remain unchanged
    else:
        uppercase_result += char
# print the uppercase version
print(uppercase_result)