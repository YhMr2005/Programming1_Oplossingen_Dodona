# https://dodona.ugent.be/nl/courses/1286/series/14345/activities/819600301

aantal_stapels = int(input())
aantal_munstukken = sum(range(aantal_stapels+1))
gewicht_goudstuk = int(input())
totaal_gewicht_muntstukken = int(input())
aantal_valse_muntstukken = abs(totaal_gewicht_muntstukken - gewicht_goudstuk * aantal_munstukken)
print(aantal_valse_muntstukken)
