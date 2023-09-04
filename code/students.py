students = []
with open("names.txt","r") as file:
    for line in sorted(file):
        name,age = line.rstrip().split(",")
        student = {"name":name, "age":age}
        students.append(student)
        print(f"{name},{age}")
    print(students)

def sort_name(student):
    return student['name']

def sort_age(student):
    return student['age']

for student in sorted(students,key=sort_name):
    print(f"{student['name']},{student['age']}")

for student in sorted(students,key=sort_age):
    print(f"{student['name']},{student['age']}")

for student in sorted(students,key=lambda student: student['name'], reverse = True):
    print(f"{student['name']},{student['age']}")