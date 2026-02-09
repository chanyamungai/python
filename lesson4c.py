# A for loop can also be used to iterate through a tuple a list or even dictionary

name="Chanya"

for letter in name :
    if letter == "n":
        print("This is letter n")
    else:
        print(letter)

print("========================")   
# Below is a list of counties
counties=["Nairobi","Mombasa","Kisumu","Nakuru","Eldoret","Kajiado","Machakos","Meru","Embu"]

print(counties)

for county in counties:
    print(county)

print("========================") 
for county in counties:
    if "Nakuru" in counties:
        print("County Found")
        break
    else :
        print("County not found")

print("========================") 
# The for loop can be used to itratetrough a dictionary

player={
    "Name":"Mbappe",
    "Age" : "25",
    "teams" : ["PSG","Monaco","France"],
    "Nationality": "French"
}

for key in player:
    print(key)

for value in player:
    print(player[value])

print("========================") 
# loop throught the teams he has played for
for teams in player["teams"]:
    print(teams)