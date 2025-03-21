# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# initialize variable to store how often the number repeats

# create infinite loop to continuously ask user to input numbers
# count how often the number occur
# add 1 to count if the number already exists
# initialize count to 1 if it's the first appearance
# stop the program when there's invalid input

# initialize max frequency and most frequent number

# identify the number that has most duplicates
# if count is greater than max frequency, update max frequency to that value
# find the number(s) with that maximum frequency
# if a number's frequency match to the max frequency, add it to most frequent numbers

# print the most frequent number/s


num_count = {}
while True:
    try:
        num = float(input("Enter a number: "))
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    except ValueError:
        print("Invalid input!")
        break

max_frequency = 0
most_freqnt_nums = []

for count in num_count.values():
    if count > max_frequency:
        max_frequency = count
for num, count in num_count.items():
    if count == max_frequency:
        most_freqnt_nums.append(num)

print(f"The most frequent number(s): {most_freqnt_nums} (Frequency: {max_frequency})")