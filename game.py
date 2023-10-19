#!/usr/bin/env python

import os
import random 
path="C:\\Users\\Admin\\Downloads\\LAGUU"
files=os.listdir(path)
d=random.choice(files)
os.startfile(d)

import random

def main():
    """Teka nama artis."""
    print("Teka Artis!")

    artis = [
        "XPDC",
        "SUDIRMAN",
        "UKAYS",
        "SLAM",
        "SEARCH"
        ]

    x = random.choice(artis)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("Apa nama artis yang dimainkan?"))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()