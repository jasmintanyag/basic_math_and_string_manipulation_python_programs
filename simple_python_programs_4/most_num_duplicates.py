# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# initialize variable to store how often the number repeats
num_count = {}
# create infinite loop to continuously ask user to input numbers
while True:
    try:
        num = float(input("Enter a number: "))
# count how often the number occur
# add 1 to count if the number already exists
        if num in num_count:
            num_count[num] += 1
# initialize count to 1 if it's the first appearance
        else:
            num_count[num] = 1
# stop the program when there's invalid input
    except ValueError:
        print("Invalid input!")
        break

# initialize max frequency and most frequent number
# identify the number that has most duplicates
# if count is greater than max frequency, update max frequency to that value

# find the number(s) with that maximum frequency
# if a number's frequency match to the max frequency, add it to most frequent numbers

# print the most frequent number/s