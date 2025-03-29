# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# ask user to input text/string
text = input("Enter a text: ")
# ask again to input the prefix they want to check
prefix = input("Enter prefix to check: ")
# checks if the extracted prefix is equal to the inputted prefix
if text[:len(prefix)] == prefix:
# if yes, the condition is true
# else, it is false
# print the result