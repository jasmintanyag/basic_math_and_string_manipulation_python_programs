# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# initialize total number of sum to 0 before the loop
total_sum = 0
# loop from 1 to 10
# ask the user to enter a number 10 times (since the range is 10)
# convert the input to a float
for i in range(10):
    num = float(input(f"Enter a number ({i+1}):  "))
# add the number to total
    total_sum += num
# print the total sum
print(total_sum)