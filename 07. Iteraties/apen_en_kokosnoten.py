# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/967703372

aantal_piraten = int(input())

kokosnoten_stapel = aantal_piraten
vermenigvuldiger = 1

while True:
    kokosnoten_stapel += 1
    for i in range(aantal_piraten):
        kokosnoten_stapel = (kokosnoten_stapel - 1) * ((aantal_piraten-1) / aantal_piraten)
        if kokosnoten_stapel % aantal_piraten != 1:
            break
    if kokosnoten_stapel % aantal_piraten == 1:
        break

    vermenigvuldiger += 1
    kokosnoten_stapel = aantal_piraten * vermenigvuldiger

print(aantal_piraten * vermenigvuldiger + 1)
