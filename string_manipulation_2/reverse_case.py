# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# ask user to input a text/string
text = input("Enter a text: ")
# initialize empty string to store the converted result
reverse_case = ""
# create for-loop in every character in text/string
for char in text:
# checks if char is an uppercase, then convert it to lowercase
    if 'a' <= char <= 'z':
        reverse_case += chr(ord(char) - 32)
# checks if char is an lowercase, then convert it to uppercase
    elif 'A' <= char <= 'Z':
        reverse_case += chr(ord(char) + 32)
# else, remain unchange
    else:
        reverse_case += char
# print the swapcase version
print(reverse_case)