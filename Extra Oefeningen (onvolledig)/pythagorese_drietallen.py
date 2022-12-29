# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/683768040

getal = int(input())
drietallen = []

for a in range(1, getal//2):
    for b in range(1, getal//2):
        for c in range(1, int(getal/(3/2))):
            if b >= a and c >= b:
                if a + b + c == getal and a**2 + b**2 == c**2:
                    drietallen.append((a, b, c))

for drietal in drietallen:
    print(drietal)