# Python List
# A list is a collection of items that are ordered in a certin way
# A list is introduced by the use of square brackets []
# The items of a list are stored inside of indexes. Note: In programming we start counting from index 0 
# A list is mutuable i.e the contents of the list can be changed

cars =["BWM","Benze","Hiance","Prado","Probox","Mclarel","Range"]

print(cars)
print(type(cars))

# Accesing items of a list
print(cars[2])
print("The car on index four is:",cars[4])


# List slicing - This is creating a list from a given bigger list
print(cars[4:])

# Print from index zero to index three
print(cars[:4])

# Printing from hiance to probox
print(cars[2:5])

# List- mutablity
# we use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("Subaru")
print(cars)

# We use the pop function to remove items at the end of the list
cars.pop()
print(cars)

# We can use anindex to add items to a list
cars[5] =Pajero
print(cars)

# We can use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

del cars[4]
print(cars)

cars.pop(4)
print(cars)

cars.remove("BMW")
print(cars)