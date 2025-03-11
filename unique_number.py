# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# initialize the variables for storing the numbers
num_list = []       # list to store user input
unique_nums = []    # list to store unique numbers
num_counts = {}     # dictionary to store number counts
# ask user to input 10 numbers, using for loop
# convert into integer
for i in range(10):
    entered_num = int(input(f"Enter number ({i+1}): "))
# add the entered number into the list
    num_list.append(entered_num)
# check how many times the number appear
# check if the number appeared only once
# if appeared only once, add it to the list of unique numbers
# print the unique number/s