people = [ 
    {"name":"Dhana", "house":"Maryland"},
    {"name":"Prashant", "house":"VA"}
]

persons_list = [ "Dhana", "Prashant"]
persons_dict = {"name":"Dhana" , "name1":"Prashant"}

"""def func(person):
    abc = []
    abc= people["name"][0]
    print(abc)
"""

#func(people)

abc=sorted(persons_list)
print(abc)
abc=persons_list.sort()
print(persons_list.sort())

print(persons_dict.sort(key="name"))