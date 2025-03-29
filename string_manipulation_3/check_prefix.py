# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# ask user to input text/string
# ask again to input the prefix they want to check
# checks if the extracted prefix is equal to the inputted prefix
# if yes, the condition is true
# else, it is false
# print the result

text = input("Enter a text: ")
prefix = input("Enter prefix to check: ")
if text[:len(prefix)] == prefix:
    matched_to_prefix = True
else:
    matched_to_prefix = False
print("Prefix matched: ", matched_to_prefix)