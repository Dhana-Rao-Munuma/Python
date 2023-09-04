names = []

for a in range(2):
    name = input("enter the name:")
    names.append(name)

file = open("names.txt","a")

for name in sorted(names):
    #print(name)
    file.write(name)
    file.write("\n")
    file.write(f"{name}\n")

file.close()

with open("names.txt","w") as file:
    for name in sorted(names):
        file.write(f"{name}\n")

with open("names.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line,end="")
    print()
    for line in lines:
        print(line.rstrip())
    print(lines)

with open("names.txt","r") as file:
    for line in file:
        print(line.rstrip())