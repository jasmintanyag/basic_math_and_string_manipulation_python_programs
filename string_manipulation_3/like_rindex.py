# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# ask user to input a string
# ask again to input the substring to find
# initialize the index variable
# loop through the string from left to right
# check if substring matches the current position
# store the index and stop the loop
# if index is still -1, it means the substring was not found
# else, print the result if found

text = input("Enter a text: ")
substring = input("Enter the substring to find: ")
index = -1
# PRINT INPUT VALUES
print(f"Text: '{text}', Substring: '{substring}'")

for i in range(len(text) - len(substring) -1, -1):
    print(f"Checking index {i}: '{text[i:i+len(substring)]}'")  # Debugging line
    if text[i:i+len(substring)] == substring:
        index = i
        break

if index == -1:
    print("Substring not found :(")
else:
    print(index) 

# NOT YET FIXED