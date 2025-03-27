# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# ask user to input a text/string
# initialize empty string to store the converted result
# create for-loop in every character in text/string
# checks if char is an uppercase, then convert it to lowercase
# checks if char is an lowercase, then convert it to uppercase
# else, remain unchange
# print the swapcase version

text = input("Enter a text: ")
reverse_case = ""
for char in text:
    if 'a' <= char <= 'z':
        reverse_case += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        reverse_case += chr(ord(char) + 32)
    else:
        reverse_case += char
print("Swapcase: ", reverse_case)