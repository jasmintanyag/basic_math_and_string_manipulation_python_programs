# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# initialize variable to store user input
entered_num = []
# ask user to input 10 numbers using for loop
for i in range(10):
    num = input(f"Enter number ({i+1}): ")
# convert into integer
# check if num is in the list, if not, add it
# print the numbers