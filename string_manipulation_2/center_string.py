# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# ask user input text/string
text = input("Enter a text: ")
# ask again for their targeted length
target_length = int(input("What is your targeted length? "))
# if the string entered is shorter than their targeted length, add spaces to the right side
if len(text) < target_length:
# calculate the total spaces needed to center the text
    total_space = target_length - len(text)
# divide spaces equally to left and right
    left_space = total_space // 2
    right_space = total_space - left_space
# print the string in the center