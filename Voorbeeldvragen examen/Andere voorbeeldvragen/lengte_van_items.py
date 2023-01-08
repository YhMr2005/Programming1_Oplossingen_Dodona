invoer = input()

# Verwijder leestekens
for char in invoer:
    if not char.isalpha() and char != " ":
        invoer = invoer.replace(char, '')

# Lijst van woorden
lijst = invoer.split()
lijst = [woord.lower() for woord in lijst]

# 1) Set van unieke woorden
set_van_woorden = set(lijst)
print(set_van_woorden)

# 2) Aantal woorden langer dan 10 tekens
aantal_langer_dan_10 = len([woord for woord in set_van_woorden if len(woord) > 10])
print(f"Er zijn {aantal_langer_dan_10} woorden die langer zijn dan 10 tekens")

# 3) Aantal woorden met lengte veelvoud van 3
aantal_veelvoud_3 = len([woord for woord in set_van_woorden if len(woord) % 3 == 0])
print(f"Er zijn {aantal_veelvoud_3} woorden waarvan de lengte een veelvoud is van 3")

# 4) Gemiddelde lengte van de woorden
gem_lengte = sum(len(woord) for woord in set_van_woorden) / len(set_van_woorden)
print(f"De gemiddelde lengte van alle unieke woorden is: {gem_lengte:.2f} tekens")
