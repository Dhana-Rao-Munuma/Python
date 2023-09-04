# Sample dictionary with values
sample_dict = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "David": 28
}

# Sorting the dictionary by values in ascending order
sorted_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

# Printing the sorted dictionary
for key, value in sorted_dict.items():
    print(key, value)
