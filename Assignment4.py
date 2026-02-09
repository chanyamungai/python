# Lesson4task1
# 1. Using a For Loop Print from 2000 to 2024
for number in range(2000,2025,4):
    print(number)

# Lesson4Task3.py 
#  Create a List of Colors Blue, Green, Red, Pink , Black- Using a for Loop, Loop through the colors
colors =["Blue","Green","Red","Pink","Black"]
for color in colors:
    print(color)

#  Lesson4Task2.py
# Using a While Loop Print from 20 to 1
# Lesson4Task2.py

number = 20
while number >= 1:
    print(number)
    number=number-1
# A function is a block of code which only runs when it is called.
# A function is defined using the def keyword, followed by a function name and parentheses:
def greet():
    print("Hello Chanya")

greet()

# Function with parameters-parameters are values you pass into a function
def greet(name):
    print("Hello", name)

greet("Chanya")

# Fuction helps avoid repetion of codes
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 3)
add_numbers(10, 20)

