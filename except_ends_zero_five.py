# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# create a for loop, from numbers 0 to 100
for num in range(101):
# check if the number is not divisible by 5
    if num % 5 != 0:
# if not, print the numbers
        print(num, end= " ")