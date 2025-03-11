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
for entered_num in num_list:
    num_counts[entered_num] = num_counts.get(entered_num, 0)
# check if the number appeared only once
for entered_num in num_list:
    if num_counts[entered_num] == 1:
# if appeared only once, add it to the list of unique numbers
        unique_nums.append(entered_num)
# print the unique number/s