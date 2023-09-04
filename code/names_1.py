import sys

if len(sys.argv) < 2:
    sys.exit("Not enough arguments")

for arg in sys.argv[1:]:
    print("Name is ",arg)

"""
try:
    print("name is ", sys.argv[0], sys.argv[1])
except IndexError:
    print("Not enough arguments")
"""