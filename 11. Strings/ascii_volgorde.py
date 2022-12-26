# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/335876740

# Oplossing 1: zonder gebruik van lijst
tekst = input()
uitvoer = ''

while len(tekst) != 0:
    kleinste = 'z'
    for char in tekst:
        if char < kleinste:
            kleinste = char
    uitvoer += kleinste
    tekst = tekst.replace(kleinste, '', 1)

print(uitvoer)

# Oplossing 2: met gebruik van een lijst
# tekst = input()
# lijst_van_tekst = [letter for letter in tekst]
# print("".join(sorted(lijst_van_tekst)))