# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

# ask user to input 2 numbers
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
# check if the second number is 0
# if zero, print "Cannot divide by zero."
if num2 == 0:
    print("Cannot divide by zero.")
# else, perform a floor division
# convert the result into integer