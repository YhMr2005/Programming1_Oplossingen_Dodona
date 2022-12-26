# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/1246292246

verschuiving = int(input())

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(alfabet)

aanpassing = 0

if verschuiving < 0:
    aanpassing = verschuiving

for i in range(verschuiving, len(alfabet) + aanpassing):
    print(alfabet[i], end="")

for i in range(0, verschuiving):
    print(alfabet[i], end="")

print("")