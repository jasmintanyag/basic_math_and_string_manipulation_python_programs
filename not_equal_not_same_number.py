# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

'''
ask user to input 2 numbers
use if statement to check if the 2 numbers are not equal
print "Not Equal" if the 2 numbers are not the same
'''

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num1 != num2:
    print("Not Equal")