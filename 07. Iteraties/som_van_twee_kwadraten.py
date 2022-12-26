# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/191240337
from math import sqrt

start = int(input())
end = int(input())
kwadraten = []

for getal in range(start, end+1):
    for x in range(int(sqrt(getal)+1)):
        for y in range(getal+1):
            if x**2 + y**2 == getal and (y,x) not in kwadraten:
                kwadraten.append((x,y))

for paar in kwadraten:
    print("{} ** 2 + {} ** 2 = {}".format(paar[0], paar[1], paar[0]**2+paar[1]**2))