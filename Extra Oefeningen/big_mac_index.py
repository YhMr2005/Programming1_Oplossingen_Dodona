# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1131866318

def waardering(prijs_bigmac, wisselkoers):
    prijs_usa = 4.07
    bigmac_index = prijs_bigmac / prijs_usa
    verhouding = ((bigmac_index - wisselkoers) / wisselkoers) * 100

    if verhouding <= -25:
        waardering = "sterk ondergewaardeerd"
    elif verhouding <= -5:
        waardering = "ondergewaardeerd"
    elif verhouding <= 5:
        waardering = "ongeveer gelijk"
    elif verhouding <= 25:
        waardering = "overgewaardeerd"
    else:
        waardering = "sterk overgewaardeerd"
    
    return waardering

def wisselkoersanalyse(prijs_bicmac, wisselkoers):
    eerste_spatie = prijs_bicmac.find(" ")
    prijs = float(prijs_bicmac[:eerste_spatie])
    munteenheid = prijs_bicmac[eerste_spatie+1:]
    waardering_munteenheid = waardering(prijs, wisselkoers)
    return f"De {munteenheid} is {waardering_munteenheid} ten opzichte van de dollar."
