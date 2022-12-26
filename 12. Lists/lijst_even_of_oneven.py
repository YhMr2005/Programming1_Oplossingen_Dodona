# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/1624746422

aantal_cijfers = int(input())
even = []
oneven = []
for i in range(aantal_cijfers):
    getal = int(input())
    if getal % 2 == 0:
        even.append(getal)
    else:
        oneven.append(getal)

print(even)
print(oneven)