import csv
students = []
with open("names.txt","r") as file:
    f_csv = csv.reader(file)

    for line in f_csv:
        print(line)
        print(f"{line[0]},{line[1]}")
        student={"name":line[0],"age":line[1]}
    
    #for name,age in f_csv:
    #    student={"name":name,"age":age}
        
        students.append(student)
        
for student in students:
    print(f"{student['name']},{student['age']}")


students = []
with open("names_1.txt","r") as file:
    f_csv = csv.DictReader(file)
    for line in f_csv:
        print(line)
        #student={"name":line["name"],"age":line["age"]}
        #students.append(student)
        students.append(line)

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']},{student['age']}")
