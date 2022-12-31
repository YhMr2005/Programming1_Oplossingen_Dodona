# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/548200706

punten = [int(input()), int(input()), int(input())]

if sorted(punten) != punten:
    print("ongeldige invoer")

elif len([p for p in punten if p >= 50]) == 3:
    print("geslaagd")

elif len([p for p in punten if p >= 50]) == 2 \
    and min(punten) >= 40 and sum(punten) >= 150:
        print("gedelibereerd")
else:
    print("niet geslaagd")