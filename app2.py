# While loop

# Guessing Game

# secret_number = 8
# Guess_Count =0
# Guess_Limit = 3
# while Guess_Count<Guess_Limit:
#     guess = int(input("Guess: "))
#     Guess_Count+=1
#     if guess == secret_number:
#         print("You Won")
#         break
# else:
#     print("You Failed")

# Basic while loop

# i = 1
# while i<6:
#     print(i * '*')
#     i+=1
# print('Completed')

# For loop

# prices = [20, 30, 45, 32]
#
# sum = 0
#
# for price in prices:
#     sum = sum+price
#
# print(f'Total: {sum}')


# Nested loop

# numbers = [2,2,2,2,2,2,2,5]
#
# for x in numbers:
#     output = ''
#     for y in range(x):
#         output+='*'
#     print(output)

# List are mutable

# names = ['john', 'mary', 'joe', 'peter']
#
# print(names[:])

# program to find max number from list

# numbers = [2,3,4,5,3,44,34,65,77,99,2,3,4]
# max = numbers[0]
#
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# 2d list - two dimensional

# matrix = [
#     [1,2,4],
#     [4,5,6],
#     [4,6,7]
# ]
#
# for col in matrix:
#     for item in col:
#         print(item*2)


# List Methods

# 1. append- which adds numbers to the list to the last
# 2. insert- which adds number to the front of list
# 3. remove- which removes a number from list
# 4. clear- which clears a total list

# it removes duplicates from the list

# numbers = [3,3,4,3,5,6,1,2,7,7,6,5,8,9]
#
# final = list(set(numbers))
# print(final)

# tuples- this is immutable

# Dictionaries- can store key value pairs

# customers = {
#     'name': 'john',
#     'age': 26,
#     'is_verified': True
# }
#
# customers['is_alive'] = True
#
# print(customers['is_alive'])

# Converting number into string

# phone = input('Phone: ')
#
# character = {
#     '1' : 'One',
#     '2' : 'Two',
#     '3' : 'Three',
#     '4' : 'Four'
# }
# output = ''
# for ch in phone:
#
#     output+=character.get(ch) + ' '
# print(output)


# Emoji Convertor

# message = input('>')
# words = message.split(' ')
# emojis = {
#     ':)' : '😀',
#     ':(' : '🙁'
# }
# output = ""
# for word in words:
#     output+= emojis.get(word, word) + " "
# print(output)

# Functions

# Exceptions- it is a kind of error that crashes our program

# try:
#     age = int(input("What is ur age? "))
#     print(age)
# except ValueError:
#     print("Invalid input")

# Classes

# We use classes to define new types, these types can have
# methods that we define in the body of the class and they can
# also have attributes that we can set anywhere in our programs


# class Point:
#     def move(self):
#         print('move')
#     def draw(self):
#         print('draw')
#
# result = Point()
# result.x = 100
# print(result.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print('yes')
#
# result = Person('sai')
# print(result.name)
# result.talk()

# inheritance- it is a mechanism of reusing the code
















































