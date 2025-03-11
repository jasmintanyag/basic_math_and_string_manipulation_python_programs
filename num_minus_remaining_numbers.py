# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

'''
initialize total difference to 0 before the loop
loop from 1 to 10
ask the user to enter a number 10 times (since the range is 10)
convert the input to a float
if it's the first number, add it to total difference
else, subract the number from total difference
print the total difference
'''

total_diff = 0
for i in range(10):
    num = float(input(f"Enter a number ({i+1}):  "))
    if i == 0:
        total_diff += num
    else:
        total_diff -= num
print(f"The total difference is: {total_diff}")