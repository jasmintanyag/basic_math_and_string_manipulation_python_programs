# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# ask user to input a string
user_inp =  input("Enter a string: ")
# initialize a counter
i = 0
# create while-loop
# if i is less than the length of s, and the character at i is space, 
while i < len(user_inp) and user_inp[i] == " ":
# move to the next character until a non-space character is found
    i += 1
# print starting from index i
print("Result: ", user_inp[1:])