import sys

try:
    print("name is ", sys.argv[0], sys.argv[1])
except IndexError:
    print("Not enough arguments")
