# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# ask user input numbers/string with spaces in beginning
nums = input("Enter a number w/ spaces at beginning: ")
# ask again for their targeted length
target_length = int(input("What is your targeted length? "))
# if the string entered is shorter than their targeted length, change the spaces into zeroes
# print the modified string / result