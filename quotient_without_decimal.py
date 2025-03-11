# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

'''
ask user to input 2 numbers
check if the second number is 0
if zero, print "Cannot divide by zero."
else, perform a floor division
convert the result into integer
'''

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num2 == 0:
    print("Cannot divide by zero.")
else:
    print(f"The quotient of the two number is: {int(num1 // num2)}")