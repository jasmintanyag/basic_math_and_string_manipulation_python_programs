# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# ask user to input a string
text = input("Enter a string: ")
# ask again to input the suffix they want to remove
suffix = input("Enter the suffix you want to remove: ")
# check if the text/string they inputted ends with the suffix
if text.endswith(suffix):
# if yes, remove it by slicing from the length of suffix
    print("Removed Prefix Result: ", text[:-len(suffix):])
# if not, print the original text 