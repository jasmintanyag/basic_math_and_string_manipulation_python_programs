# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# ask user input text/string
# ask again for their targeted length
# if the string entered is shorter than their targeted length, add spaces to the left side
# print the modified string / result

text = input("Enter a text: ")
target_length = int(input("What is your targeted length? "))
if len(text) < target_length:
    text = " " * (target_length - len(text)) + text
print("Right-justified result:", text)