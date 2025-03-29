# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# ask user to input a text/string
# assume that the text is all lowercase letters initially
# create for-loop in every character in text/string
# check if char is in uppercase
# if at least one uppercase letter is found, set it to false then exit the loop
# print True if all characters are lowercase

text = input("Enter a text: ")
all_lowercase = True
for char in text:
    if 'A' <= char <= 'Z':
        all_lowercase = False
        break
print("The text is all LOWERCASE: ", all_lowercase)