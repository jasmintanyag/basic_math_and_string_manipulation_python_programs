# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# ask user input numbers/string
# ask again for their targeted length
# make sure that the input is string
# if the string entered is shorter than their targeted length, subtract the length of input from the targeted lenth
# add the required zeroes at the beginning
# print the modified string / result

nums = input("Enter a number(s): ")
target_length = int(input("What is your targeted length? "))
nums = str(nums)

if len(nums) < target_length:
    zeroes = target_length - len(nums)
    nums = '0' * zeroes + nums

print("Zero-filled result:", nums)