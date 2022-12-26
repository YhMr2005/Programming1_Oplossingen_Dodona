# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/719095937


getal = int(input())

eerste_lijn = (" " * len(str(getal)) + " |")
for i in range(1, getal+1):
    ruimte_hoofd = len(str(i*getal))
    eerste_lijn += " " + f"{str(i):>{ruimte_hoofd}}"

lengte = len(eerste_lijn)
print(eerste_lijn)
print("=" * lengte)

ruimte_eerste_kolom = len(str(getal))

for rij in range(1, getal+1):
    print(f"{str(rij):>{ruimte_eerste_kolom}}" + " |", end="")
    for kolom in range(1, getal+1):
        ruimte_kolom = len(str(getal*kolom))
        print(" " + f"{str(rij*kolom):>{ruimte_kolom}}", end="")
    print("") 