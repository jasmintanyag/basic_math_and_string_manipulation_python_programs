# Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.

'''
ask user to input 2 numbers
check if the second number is 0
if zero, print "Cannot divide by zero."
print the quotient of two numbers
'''

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num2 == 0:
    print("Cannot divide by zero.")
else:
    print(f"The quotient of the two number is: {num1 / num2}")