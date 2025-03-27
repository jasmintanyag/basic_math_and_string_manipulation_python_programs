# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# ask user to input text/string
text = input("Enter a text: ")
# ask again to input the suffix they want to check
suffix = input("Enter suffix to check: ")
# checks if the extracted suffix is equal to the inputted suffix
if text[-len(suffix): ] == suffix:
# if yes, the condition is true
    matched_to_suffix = True
# else, it is false
else:
    matched_to_suffix = False
# print the result
print(matched_to_suffix)