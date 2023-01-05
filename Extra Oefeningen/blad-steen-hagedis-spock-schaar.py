# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1647887074

speler1 = input()
speler2 = input()

handgebaar_wint_van = {
    "schaar": ["blad", "hagedis"],
    "blad": ["steen", "Spock"],
    "steen": ["hagedis", "schaar"],
    "hagedis": ["Spock", "blad"],
    "Spock": ["schaar", "steen"]
}

if speler1 == speler2:
    print("gelijkspel")
elif speler2 in handgebaar_wint_van[speler1]:
    print("speler1 wint")
else:
    print("speler2 wint")