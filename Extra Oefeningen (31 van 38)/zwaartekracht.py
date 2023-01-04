# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1370867069

# Oplossing 1: zonder gebruik van dictionary
from sys import exit

hemellichamen = ('de maan', 'Jupiter', 'Mars', 'Venus', 'Neptunus')

gewicht = float(input("Geef je gewicht in (kg): "))
hemellichaam = input("Op welk hemellichaam ben je? ")

if hemellichaam not in hemellichamen:
    print("Ongeldige invoer!")
    exit()

if hemellichaam == "de maan":
    gewicht *= 0.166
elif hemellichaam == "Jupiter":
    gewicht *= 2.36
elif hemellichaam == "Mars":
    gewicht *= 0.37
elif hemellichaam == "Venus":
    gewicht *= 0.9
elif hemellichaam == "Neptunus":
    gewicht *= 1.12
    
print(f"Op {hemellichaam} weeg je {gewicht} kilogram.")

# Oplossing 2: met gebruik van een dictionary
# from sys import exit

# hemellichamen = {
#     'de maan': 0.166,
#     'Jupiter': 2.36,
#     'Mars': 0.37,
#     'Venus': 0.9,
#     'Neptunus': 1.12
# }

# gewicht = float(input("Geef je gewicht in (kg): "))
# hemellichaam = input("Op welk hemellichaam ben je? ")

# if hemellichaam not in hemellichamen:
#     print("Ongeldige invoer!")
#     exit()

# else:
#     print(f"Op {hemellichaam} weeg je {gewicht*hemellichamen.get(hemellichaam)} kilogram.")
