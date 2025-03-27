# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# ask user to input a text/string
text = input("Enter a text: ")
# assume that the text is all uppercase letters initially
all_uppercase = True
# create for-loop in every character in text/string
for char in text:
# check if char is in lowercase
    if 'a' <= char <= 'z':
# if at least one lowercase letter is found, set it to false then exit the loop
        all_uppercase = False
        break
# print True if all characters are uppercase; false if not
print(all_uppercase)