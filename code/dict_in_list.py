dict_in_list = [
    {"Name":"Dhana", "Color":"Blue", "Food":"Meals"},
    {"Name":"Tejansh", "Color":"Red", "Food":"Fruits"},
    {"Name":"Hetika", "Color":"Pink", "Food":"Cerelac"}
]

for dict in dict_in_list:
    for key in dict:
        print(key, dict[key])
