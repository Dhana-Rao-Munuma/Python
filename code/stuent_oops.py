def main():
    #name = get_name()
    #house = get_house()
    
    #name, house = get_student()
    #print(f"{name} from {house}")

    student = get_student()
    print(f"{student[0]} from {student[1]}")
def get_name():
    return input("Name:")

def get_house():
    return input("House:")

def get_student():
    name = get_name()
    house = get_house()
    #return name,house
    return (name,house)

if __name__ == "__main__":
    main()