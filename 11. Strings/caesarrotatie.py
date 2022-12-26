# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/105361566

verschuiving = int(input())
woord = input()

alfabet = "ZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBA"


uitvoer = ""

for char in woord:
    if char.isalpha():
        if char.isupper():
            uitvoer += alfabet[alfabet.find(char)+verschuiving]
        elif char.islower():
            uitvoer += alfabet.lower()[alfabet.lower().find(char)+verschuiving]

    else:
        uitvoer += char

print(uitvoer)