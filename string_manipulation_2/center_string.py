# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# ask user input text/string
# ask again for their targeted length
# if the string entered is shorter than their targeted length, add spaces to the right side
# calculate the total spaces needed to center the text
# divide spaces equally to left and right
# add spaces to left and right side
# print the string in the center

text = input("Enter a text: ")
target_length = int(input("What is your targeted length? "))
if len(text) < target_length:
    total_space = target_length - len(text)
    left_space = total_space // 2
    right_space = total_space - left_space
    text = " " * left_space + text + " " * right_space
print(f"Result: '{text}'")