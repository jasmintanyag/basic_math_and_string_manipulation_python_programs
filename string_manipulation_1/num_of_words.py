# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

# ask user input a complete statement
# print the number of words in the input

statement = input("Enter a complete statement: ")
print("Number of words: ", len(statement.split()))