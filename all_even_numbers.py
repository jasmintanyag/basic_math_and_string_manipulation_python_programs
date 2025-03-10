# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

'''
create a for loop, from numbers 0 to 100
check if even number
print all even numbers
'''

for num in range(101):
    if num % 2 == 0:
        print(num, end = " ")