# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# initialize variable to store user input, (empty list)
list_of_all_nums = []
# create infinite loop to continuously ask user to input numbers
while  True:
    try:
        num = float(input("Enter a number: "))
# add the entered number to the list
# if user entered an invalid input, stop the program
# sort the entered numbers from highest to  lowest using sort(reverse) function
# display the numbers from highest to  lowest