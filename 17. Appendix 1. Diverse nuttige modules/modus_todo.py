# https://dodona.ugent.be/nl/courses/1286/series/14368/activities/1509774218

from statistics import mean, median
from collections import Counter

getallen = []

nieuw_getal = int(input("Geef een getal (0 om te stoppen): "))
while nieuw_getal != 0:
    getallen.append(nieuw_getal)
    nieuw_getal = int(input("Geef een getal (0 om te stoppen): "))

gemiddelde = mean(getallen)
mediaan = median(getallen)

c = Counter(getallen)
if all(value == 1 for value in c.values()): # Alle getallen komen exact 1 keer voor.
    modus = "Er is geen modus, alle getallen zijn uniek."
else:
    modus_lijst = [c.most_common(1)[0][0]] # Meest voorkomend getal
    for getal in c:
        if c[getal] == c.most_common(1)[0][1] and getal not in modus_lijst:
            modus_lijst.append(getal) # Voeg toe aan modus_lijst als het evenvaak voorkomt als het meest voorkomend getal.
            print(getal)
    modus = ", ".join(str(getal) for getal in modus_lijst)

print(f"Gemiddelde: {gemiddelde}\nMediaan: {mediaan}\nModus: {modus}")