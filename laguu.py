#!/usr/bin/env python

import random, os
music_dir = "C:\\Users\\Admin\\Downloads\\LAGUU"
songs = os.listdir(music_dir)
song = random.randint(0,len(songs))

#Prints The Song Name
print(songs[song])

os.startfile(os.path.join(music_dir, songs[0]))


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