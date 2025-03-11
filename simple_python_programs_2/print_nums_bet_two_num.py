# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

'''
ask user to input 2 numbers
convert into integer
if num1 is larger than num2, swap their values
create loop to get the numbers between 1st num and 2nd num
print the numbers in between
'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 > num2:
    num1, num2 = num2, num1
for numbers in range(num1 + 1, num2):
    print(numbers, end= " ")