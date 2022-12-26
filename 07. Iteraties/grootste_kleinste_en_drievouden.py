# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/2109616883

# Oplossing 1: zonder gebruik van lijst
grootste_getal = 0
aantal_drievouden = 0

nieuw_getal = int(input())
kleinste_getal = nieuw_getal
grootste_getal = nieuw_getal
if nieuw_getal % 3 == 0:
    aantal_drievouden += 1

for i in range(9):
    nieuw_getal = int(input())
    if nieuw_getal % 3 == 0:
        aantal_drievouden += 1
    if nieuw_getal <= kleinste_getal:
        kleinste_getal = nieuw_getal
    if nieuw_getal >= grootste_getal:
        grootste_getal = nieuw_getal

print("grootste:", grootste_getal)
print("kleinste:", kleinste_getal)
print("drievouden:", aantal_drievouden)

# Oplossing 2: met gebruik van een lijst
# getallen = []
# for i in range(10):
#     getallen.append(int(input()))

# print("grootste:", max(getallen))
# print("kleinste:", min(getallen))
# print("drievouden:", len([getal for getal in getallen if getal % 3 == 0]))