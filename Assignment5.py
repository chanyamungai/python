# Create a function that:Takes no parameters Uses arithmetic operators to calculate the area of a rectangle Prints the result
def area ():
    length=20
    width=30
    area=length*width
    print("The area of the rectangle is:",area)

area()

print("==================")
# Create a function that: Accepts two numbers as parameters, Returns their sum, difference, product, and division
def calculation(x,y):
    sum=x+y
    difference=x-y
    product=x*y
    division=x/y
    print("The sum of the number is",sum)
    print("The difference of the number is",difference)
    print("The product of the number is",product)
    print("The division of the number is",division)

calculation(20,5)

# Write a function that: Accepts a number (use input function)Checks whether the number is:Positive Negative Zero

def check_number():
    number = int(input("Enter a number: "))

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

check_number()


# Write a function that: Accepts a number (Use input() function) Uses a while loop Calculates the square of numbers from 1 up to that number
def squares_up_to_n():
    n = int(input("Enter a number: ")) 
    i = 1
    while i <= n:
        print(i * i)
        i = i + 1

squares_up_to_n()



