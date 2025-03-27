# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# ask user to input a text/string
text = input("Enter a text: ")
# in the string entered; if first character is lowercase, convert it to uppercase
if text:
    first_character = text[0]
    if 'a' <= first_character <= 'z':
        first_character = chr(ord(first_character) - 32)
# for the rest of the characters; if uppercase, convert it to lowercase
# else, remain unchange
# print the result