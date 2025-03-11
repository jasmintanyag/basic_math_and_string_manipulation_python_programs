# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# initialize variable to store user input, (empty list)
list_nums = []
# create infinite loop to continuously ask user to input numbers
while True:
    try:
        num = float(input("Enter a number: "))
# add the entered number to the list
        list_nums.append(num)
# if user entered an invalid input, stop the program
# print the lowest number that has been entered