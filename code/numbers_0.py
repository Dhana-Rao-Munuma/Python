
from sys import argv, exit

numbers = [ 4, 6, 8, 2, 7, 5, 0]
found = False
if len(argv) != 2 :
    print("invalid number of arguments")
    exit(1)

val = int(argv[1])
for i in range(len(numbers)) :
    if numbers[i] == val :
        found = True
        break
if found == False :
    print(f"Value {val} Not found ")
else :
    print(f"Value {val} found at position {i} - numbers[i] is {numbers[i]} !")

exit(0)


"""
numbers = [ 4, 6, 8, 2, 7, 5, 0]
found = False
val = int(input("Value to be searched:"))
for i in range(len(numbers)) :
    if numbers[i] == val :
        found = True
        break
if found == False :
    print(f"Value {val} Not found ")
else :
    print(f"Value {val} found at position {i} - numbers[i] is {numbers[i]} !")
"""


"""
from sys import argv, exit

numbers = [ 4, 6, 8, 2, 7, 5, 0]

if 10 in numbers :
    print("Found !")
    exit(0)

print("Not Found !")
exit(1)
"""