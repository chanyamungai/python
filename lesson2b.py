# tuple is an unmutable type of a list meaning it cannot change
# To introduce a tuple we use ()

counties=("Nairobi","Mombasa","Nakuru","Eldoret","Kajiado","Kisii")

print(counties)
print(type(counties))

# Slicing of tuples
print(counties[3:])

# Accesing items of a tuple by use of indexes
print(counties[5])

# Note: Below will generate an error
# Attribute error
counties.append("Machakos")
print(counties)