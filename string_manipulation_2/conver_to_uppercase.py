# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# ask user to input a text/string
# assume that the text is all uppercase letters initially
# create for-loop in every character in text/string
# check if char is in lowercase
# if at least one lowercase letter is found, set it to false then exit the loop
# print True if all characters are uppercase; false if not

text = input("Enter a text: ")
all_uppercase = True
for char in text:
    if 'a' <= char <= 'z':
        all_uppercase = False
        break
print("The text is all UPPERCASE: ", all_uppercase)