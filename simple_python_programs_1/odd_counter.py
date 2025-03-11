# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

'''
initialize odd count to 0 before the loop
loop from 1 to 10
ask the user to enter a number 10 times (since the range is 10)
convert the input to a float
check if the number is not divisible by 2
if it is not divisible, add 1 to odd count 
print the odd count
'''

odd_count = 0
for i in range(10):
    num = float(input(f"Enter a number ({i+1}): "))
    if num % 2 != 0:
        odd_count += 1
print(f"There are {odd_count} odd number/s.")