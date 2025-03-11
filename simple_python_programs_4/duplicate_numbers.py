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
for num in num_list:
# add 1 if the number already exists
    if num in num_counts:
        num_counts[num] += 1
# initialize count to 1 if it's a new number
    else:
        num_counts[num] = 1
# check the numbers that have duplicates
for num in num_counts:
    # if the number appears more than once, add it to duplicate list
    if num_counts[num] > 1:
        duplicate_nums.append(num)
# print the number/s that have duplicate/s
print(duplicate_nums)