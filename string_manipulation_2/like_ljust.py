# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# ask user input text/string
# ask again for their targeted length
# if the string entered is shorter than their targeted length, add spaces to the right side
# print the modified string / result

text = input("Enter a text: ")
target_length = int(input("What is your targeted length? "))
if len(text) < target_length:
    text = text + " " * (target_length - len(text))
print(f"Result: '{text}'")