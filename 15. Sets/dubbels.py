# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/531231333

def dubbel(getallen):
    for getal in getallen:
        if getallen.count(getal) > 1:
            return getal
    return None

def dubbels(getallen):
    uniek = set()
    niet_uniek = set()
    for getal in getallen:
        if getallen.count(getal) == 1:
            uniek.add(getal)
        elif getallen.count(getal) > 1:
            niet_uniek.add(getal)
    return (uniek, niet_uniek)
