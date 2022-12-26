# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/396622942
from copy import deepcopy

def lijstvoorstelling(cijfers, aantal_rijen, aantal_kolommen=None):
    if aantal_kolommen is None:
        aantal_kolommen = aantal_rijen

    uitvoer = []
    for i in range(aantal_rijen):
        rij = []
        for j in range(aantal_kolommen):
            rij.append(int(cijfers[0]))
            cijfers = cijfers[1:]
        uitvoer.append(rij)

    return uitvoer

def stringvoorstelling(rooster_lijst):
    rijen = len(rooster_lijst)
    kolommen = len(rooster_lijst[0])
    cijfers = ''
    for rij in rooster_lijst:
        for cijfer in rij:
            cijfers += str(cijfer)
    return (cijfers, rijen, kolommen)

def zet(getal, cellen_posities, rooster_lijst):
    for positie in cellen_posities:
        rooster_lijst[positie[0]][positie[1]] += getal
    return rooster_lijst

def is_opgelost(rooster_lijst):
    test_waarde = rooster_lijst[0][0]
    for rij in rooster_lijst:
        for cijfer in rij:
            if cijfer != test_waarde:
                return False
    return True

def groep(cel_positie, rooster_lijst, uitvoer=None, outer_loop=True):
    rij = cel_positie[0]
    kolom = cel_positie[1]
    cijfer = rooster_lijst[rij][kolom]

    if uitvoer is None: # Maakt de lijst uitvoer leeg
        uitvoer = []

    if (rij, kolom) not in uitvoer:
        uitvoer.append((rij, kolom))

    if kolom-1 >= 0: # Check cel links
        if rooster_lijst[rij][kolom-1] == cijfer and (rij, kolom-1) not in uitvoer:
            uitvoer.append((rij, kolom-1))
            uitvoer = groep((rij, kolom-1), rooster_lijst, uitvoer, False)
    
    if kolom+1 < len(rooster_lijst[0]): # Check cel rechts
        if rooster_lijst[rij][kolom+1] == cijfer and (rij, kolom+1) not in uitvoer:
            uitvoer.append((rij, kolom+1))
            uitvoer = groep((rij, kolom+1), rooster_lijst, uitvoer, False)

    if rij-1 >= 0: # Check cel boven
        if rooster_lijst[rij-1][kolom] == cijfer and (rij-1, kolom) not in uitvoer:
            uitvoer.append((rij-1, kolom))
            uitvoer = groep((rij-1, kolom), rooster_lijst, uitvoer, False)

    if rij+1 < len(rooster_lijst): # Check cel onder
        if rooster_lijst[rij+1][kolom] == cijfer and (rij+1, kolom) not in uitvoer:
            uitvoer.append((rij+1, kolom))
            uitvoer = groep((rij+1, kolom), rooster_lijst, uitvoer, False)
    
    if outer_loop:
        return set(uitvoer)

    return uitvoer

def is_oplossing(zetten, rooster_lijst):
    rooster_lijst_kopie = deepcopy(rooster_lijst) # Mag de originele lijst niet aanpassen
    for element in zetten:
        rooster_lijst_kopie = zet(+1 if element[2] is True else -1, groep((element[0], element[1]), rooster_lijst_kopie), rooster_lijst_kopie)

    return is_opgelost(rooster_lijst_kopie)
