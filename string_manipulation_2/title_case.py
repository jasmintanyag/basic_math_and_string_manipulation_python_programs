# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# ask user to input a text/string
text = input("Enter a text: ")
# split the string in words
words = text.split()
# convert every first character of words to uppercase, while the rest of characters remain lowercase
# join the words into a string
# print the result