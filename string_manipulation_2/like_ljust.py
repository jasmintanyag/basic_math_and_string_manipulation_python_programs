# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# ask user input text/string
text = input("Enter a text: ")
# ask again for their targeted length
target_length = int(input("What is your targeted length? "))
# if the string entered is shorter than their targeted length, add spaces to the right side
if len(text) < target_length:
    text = text + " " * (target_length - len(text))
# print the modified string / result
print(text)