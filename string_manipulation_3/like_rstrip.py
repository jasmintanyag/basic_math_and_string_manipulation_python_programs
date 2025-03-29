# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# ask user to input a string
# initialize a counter from the end of the string
# create while-loop to find the last non-space character
# print the string without the spaces

text = input("Enter a string: ")  
i = len(text) - 1  
while i >= 0 and text[i] == ' ':
    i -= 1
print("Result: ", text[:i+1])