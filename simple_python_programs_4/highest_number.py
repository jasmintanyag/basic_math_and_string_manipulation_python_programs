# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# initialize variable to store user input, (empty list)
list_num = []
# create infinite loop to continuously ask user to input numbers
while True:
    try:
        num = float(input("Enter a number: "))
# add the entered number to the list
        list_num.append(num)
# if user entered an invalid input, stop the program
    except ValueError:
        print("Invalid input :(")
        break
# print the highest number that has been entered, using max()
print("The HIGHEST entered number is: ", max(list_num))