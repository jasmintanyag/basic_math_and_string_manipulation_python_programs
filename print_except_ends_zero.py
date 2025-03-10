# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# create a for loop, from numbers 0 to 100
for num in range(101):
# check if the number is not divisible by 10
# if not, print the numbers
    if num % 10 != 0:
        print(num)