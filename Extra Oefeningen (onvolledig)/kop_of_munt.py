# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/581560564

import random

random.seed(1)
aantal_worpen = int(input())

kop = 0
munt = 0
for i in range(aantal_worpen):
    if random.choice((0, 1)) == 0:
        munt += 1
    else:
        kop +=1

if munt == kop:
    print("Munt en kop zijn evenveel geworpen")
else:
    resultaat = "Munt" if munt > kop else "Kop"
    print(f"{resultaat} is meest geworpen")
