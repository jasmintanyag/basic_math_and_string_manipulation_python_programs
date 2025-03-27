# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# ask user to input text/string
# ask again to input the suffix they want to check
# checks if the extracted suffix is equal to the inputted suffix
# if yes, the condition is true
# else, it is false
# print the result

text = input("Enter a text: ")
suffix = input("Enter suffix to check: ")
if text[-len(suffix): ] == suffix:
    matched_to_suffix = True
else:
    matched_to_suffix = False
print("Suffix matched: ", matched_to_suffix)