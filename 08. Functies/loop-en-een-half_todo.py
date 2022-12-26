# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/1582865176


def getInteger(n):
    getal = int(input("Geef nummer {}: ".format(n)))
    assert 0 < getal < 1000, "De nummers moeten tussen 0 en 1000 liggen"
    return getal

x = getInteger(1)
y = getInteger(2)
assert x % y != 0 or y % x != 0, "Fout: de nummers mogen geen delers zijn"

print( "Vermenigvuldiging van", x, "met", y, "geeft", x * y )

print( "Tot ziens!" )
