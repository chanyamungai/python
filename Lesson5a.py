# Python Functions
# They are block of code/statements that performs a given task/action.They can be reused throughout the program to perform different task
# Functions are defined using the def keyword.(Define)
# We have two main type of functions i.e:
# 1.In-built funstions -> They came preinstalled with the interpreter  i.e print() pop() append() reange() e.t.c
# 2. User defined functions => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.

def greetings():
    print("Hello How are you?")
# Below we call the function by use of its name
greetings ()

print("=========================")

# Addition function
def addition():
    num1=40
    num2=20
    sum=num1+num2
    print("The sum of the number is:",sum)

addition()

print("=========================")
# Create a function that is able to multiple three values
def multiplication ():
    num3=2
    num4=4
    num5=6
    product=num3*num4*num5
    print("The product of the numbers is:",product)

multiplication()

print("=========================")
# Below is a division function
def divide ():
    number1=int(input("Enter first number: "))
    number2=int(input("Enter second  number: "))
    quotient=number1/number2
    print("The answer is",quotient)
    print("-------")

divide()

for function in range(3):
    divide( )
