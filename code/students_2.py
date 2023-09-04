import csv

name=input("enter the name:")
age=input("enter the age:")
color=input("enter the color:")

"""
with open("students_2.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","color"])
    writer.writerow([name,age,color])
"""
with open("students_2.csv","w", newline='') as file:
    writer = csv.DictWriter(file,fieldnames=["name","age","color"])
    writer.writeheader()
    writer.writerow({"name":name,"age":age,"color":color})

