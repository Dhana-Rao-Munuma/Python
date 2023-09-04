from random import choice
choice=choice(["Heads","Tails","Both"])
print(choice)

"""
import random 
choice = random.choice(["Heads","Tails"])
print("choice")
"""

from random import shuffle
cards=["A","B","C","D","E"]
shuffle(cards)
for card in cards:
    print(card)