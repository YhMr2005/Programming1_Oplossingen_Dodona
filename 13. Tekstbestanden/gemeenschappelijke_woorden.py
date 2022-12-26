# https://dodona.ugent.be/nl/courses/1286/series/14357/activities/744155174

def gemeenschappelijke_woorden(pad1, pad2, pad3):
    bestand_1 = open(pad1)
    bestand_2 = open(pad2)
    bestand_3 = open(pad3)
    set_1 = maakSetVanBestand(bestand_1)
    set_2 = maakSetVanBestand(bestand_2)
    set_3 = maakSetVanBestand(bestand_3)

    gemeenschappelijk = set_1.intersection(set_2).intersection(set_3)

    bestand_1.close()
    bestand_2.close()
    bestand_3.close()

    return gemeenschappelijk


def maakSetVanBestand(bestand):
    """
    Maakt eerst een lijst van alle woorden in het bestand, gesplitst op spaties.
    Retourneert een opgekuisde set van de lijst, dus zonder hoofdletters en leestekens.
    """
    woorden = bestand.read().split() # lijst van woorden in bestand, gesplitst op spaties
    for i in range(len(woorden)-1):
        for char in woorden[i]:
            if char.isupper(): # alles naar kleine letters
                woorden[i] = woorden[i].lower()
            if not char.isalpha(): # verwijder leestekens
                woorden[i] = woorden[i].replace(char, '')
    
    return set(woorden)
