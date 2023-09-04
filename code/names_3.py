with open("names.txt","w") as file:
    for _ in range(3):
        name = input("enter the name:")
        age = input("enter the age:")
        file.write(f"{name},{age}\n")