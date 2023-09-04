from sys import argv, exit

people = {
    "Dhana" : "240-618-9477" ,
    "Nanna" : "99510-38061"  ,
    "Anna"  : "99025-23438"
}

for name in people :
    print(people[name])

name = input("name:")

if name in people :
    number = people[name]
    print ( f"{number}")