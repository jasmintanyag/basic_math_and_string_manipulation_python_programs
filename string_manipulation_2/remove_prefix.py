# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# ask user to input a string
# ask again to input the prefix they want to remove
# check if the text/string they inputted starts with the prefix
# if yes, remove it by slicing from the length of prefix onwards
# if not, print the original text 

text = input("Enter a text: ")
prefix = input("Enter the prefix you want to remove: ")
if text.startswith(prefix):
    print("Removed Prefix Result: ", text[len(prefix):])
else:
    print("Wrong prefix, Result: ", text)