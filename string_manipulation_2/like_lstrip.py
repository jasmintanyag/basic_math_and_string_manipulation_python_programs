# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# ask user to input a string
# initialize a counter
# create while-loop
# if i is less than the length of s, and the character at i is space, 
# move to the next character until a non-space character is found
# print starting from index i

text =  input("Enter a string: ")
i = 0
while i < len(text) and text[i] == ' ':
    i += 1
print("Result: ", text[1:])