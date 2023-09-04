from sys import argv
import os

print(argv[0])
print(__file__)
print(os.path.basename(__file__))

for i in argv :
    print(i)

print()

for i in argv[1:] :
    print(i)

"""
if len(argv) == 2:
    print(f"hello {argv[1]}")
else :
    print(" Hello world !")
"""
