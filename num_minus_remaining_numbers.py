# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# initialize total difference to 0 before the loop
total_diff = 0
# loop from 1 to 10
for i in range(10):
# ask the user to enter a number 10 times (since the range is 10)
# convert the input to a float
    num = float(input(f"Enter a number ({i+1}):  "))
# if it's the first number, add it to total difference
    if num == 0:
        total_diff += num
# else, subract the number from total difference
    else:
        total_diff -= num
# print the total difference
print(total_diff)