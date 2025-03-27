# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# ask user input text/string
text = input("Enter a text: ")
# ask again for their targeted length
target_length = int(input("What is your targeted length? "))
# if the string entered is shorter than their targeted length, add spaces to the right side
# calculate the total spaces needed to center the text
# divide spaces equally to left and right
# print the string in the center