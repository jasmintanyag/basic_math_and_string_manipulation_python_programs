# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# initialize variable to store user input
list_nums = []
# create infinite loop to continuously ask user to input numbers
while True:
    try:
        num = float(input("Enter a number: "))
# check if the user already entered the same number
    # if yes, print "Duplicate"
        if num in list_nums:
            print(f"It is a DUPLICATE, {num} is already inputted.")
    # else, add on the list and print "Unique"
        else:
            list_nums.append(num)
            print("The number is UNIQUE!")
# if the user input is invalid, stop the program
    except ValueError:
        print("INVALID INPUT. Stopping the program..... :(")
        break