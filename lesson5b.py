# Functions with parameters
# They are values that get passed as arguments given to a function inside of the parenthesis

def greeting (name):
    print(f"{name} How are you?Hope everything is fine")

greeting("Chanya")

print("==============")

def message(name):
    print(f"Hello{name} we are having a general meeting on date.....Please avail yourself")

message("Joy")
message("Agnes")
# Create a function that accepts parameters to add two numbers
def addition (a,b):
    sum =a+b
    print(sum)

addition(5,6)