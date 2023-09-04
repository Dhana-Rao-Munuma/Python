import csv

titles = {}
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].lower().strip()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

for title in sorted(titles, key=lambda title_name: titles[title_name], reverse=True):
    value = titles[title]
    print(f"title {title} \t \t\t\tValue {value}")


"""
import csv

titles = {}
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].lower().strip()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1


def get_value(title_name):
    return titles[title_name]


for title in sorted(titles, key=get_value, reverse=True):
    value = titles[title]
    print(f"title {title} \t \t\t\tValue {value}")
"""
"""
import csv

titles = {}
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].lower().strip()
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

for title in sorted(titles, reverse = True):
    value = titles[title]
    print(f"title {title} \t \t\t\tValue {value}")
"""

"""
import csv

titles = set()
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].lower().strip()
        titles.add(title)

for title in sorted(titles):
    print(title)
"""
"""
import csv

titles = set()
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].lower().strip()
        titles.add(title)

for title in titles:
    print(title)
"""
"""
import csv

titles = []
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].lower().strip()
        if not title in titles:
            titles.append(title)

for title in titles:
    print(title)
"""
"""
import csv

titles = []
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if not row["Title"] in titles:
            titles.append(row["Title"])

for title in titles:
    print(title)
"""
"""
with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        print(row["Title"])
"""
"""
with open("favourites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[0])
"""