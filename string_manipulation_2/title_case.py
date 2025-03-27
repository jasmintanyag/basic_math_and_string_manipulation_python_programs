# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# ask user to input a text/string
# split the string in words
# convert every first character of words to uppercase, while the rest of characters remain lowercase
# join the words into a string
# print the result

text = input("Enter a text: ")
words_from_text = text.split()
title_cased = [word[:1].upper() + word[1:].lower() for word in words_from_text]
title_cased = " ".join(title_cased)
print("Title cased: ", title_cased)