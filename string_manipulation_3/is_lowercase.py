# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# ask user to input a text/string
text = input("Enter a text: ")
# assume that the text is all lowercase letters initially
all_lowercase = True
# create for-loop in every character in text/string
for char in text:
# check if char is in uppercase
    if 'A' <= char <= 'Z':
# if at least one uppercase letter is found, set it to false then exit the loop
        all_lowercase = False
        break
# print True if all characters are lowercase; false if not