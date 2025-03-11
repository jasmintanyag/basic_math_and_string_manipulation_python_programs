# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# initialize the variables for storing the numbers
num_list = []       # list to store user input
duplicate_nums = [] # list to store duplicate numbers
num_counts = {}     # dictionary to store number counts
# ask user to input 10 numbers, using for loop
# convert into integer
for i in range(10):
    entered_num = int(input(f"Enter number ({i+1}): "))
# add the entered number into the list
    num_list.append(entered_num)
# count how many times the number has been entered
# add 1 if the number already exists
# initialize count to 1 if it's a new number
# check the numbers that have duplicates
    # if the number appears more than once, add it to duplicate list
# print the number/s that have duplicate/s