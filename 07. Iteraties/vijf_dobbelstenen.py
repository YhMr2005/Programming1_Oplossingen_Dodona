# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1330491283

from random import randint

aantal_dobbelstenen = int(input())
steekproef = 1000000
aantal_niet_dalend = 0

for i in range(steekproef):
    aantal_stijgende_dobbelstenen = 0
    laatste_worp = 0
    for j in range(aantal_dobbelstenen):
        nieuwe_worp = randint(1,6)
        if nieuwe_worp < laatste_worp:
            break
        else:
            aantal_stijgende_dobbelstenen += 1
            laatste_worp = nieuwe_worp
    if aantal_stijgende_dobbelstenen == aantal_dobbelstenen:
        aantal_niet_dalend += 1

kans = aantal_niet_dalend / steekproef

print("P(niet-dalende reeks van {} dobbelstenen) = {:.6f}".format(aantal_dobbelstenen, kans) )
