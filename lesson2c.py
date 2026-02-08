# Dictionary is a data type that stores data in terms of key-value pair
# It is introduced by the use of {}
# The Values stored inside of a dictionary can be of any data type
# To acccess the values in a dictionay we use the keys

phonebook={
    "Benson" : "25414688224" ,
    "Mary"   :   "25422822046",
    "Stephen": "25422409315"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# Print out bennson's number
print(phonebook["Benson"])

print('========================')

player={
    "name" : "Messi",
    "age" : 40 ,
    "teams" : ["PSG","Barcelona","Argetina"],
    "more" : {
        "children" : 3 ,
        "residence" : "USA",
        "number" : ("0714688224", "0722822046","0722409315" )
    }
}
# Print Messi's 2nd number
print(player["more"]["number"][1])
# print barcelona- the second team he played for
print(player["teams"][1])