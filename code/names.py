
from sys import argv, exit

names = [ "Dhana", "Sushma", "Tejansh", "Hetika", "Rama", "Prakash"]
found = False
if len(argv) != 2 :
    print("invalid number of arguments")
    exit(1)

name = argv[1]
for i in range(len(names)) :
    if names[i] == name :
        found = True
        break
if found == False :
    print(f"name {name} Not found ")
else :
    print(f"name {name} found at position {i} - names[i] is {names[i]} !")

exit(0)


"""
names = [ "Dhana", "Sushma", "Tejansh", "Hetika", "Rama", "Prakash"]
found = False
name = input("Name to be searched:")
for i in range(len(names)) :
    if names[i] == name :
        found = True
        break
if found == False :
    print(f"name {name} Not found ")
else :
    print(f"name {name} found at position {i} - names[i] is {names[i]} !")
"""


"""
from sys import argv, exit

names = [ "Dhana", "Sushma", "Tejansh", "Hetika", "Rama", "Prakash"]

if "Dhana" in names :
    print("Found !")
    exit(0)

print("Not Found !")
exit(1)
"""