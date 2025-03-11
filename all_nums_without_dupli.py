# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# initialize variable to store user input
entered_num = []
# ask user to input 10 numbers using for loop
# convert into integer
for i in range(10):
    num = int(input(f"Enter number ({i+1}): "))
# check if num is in the list, if not, add it
    if num not in entered_num:
        entered_num.append(num)
# print the numbers