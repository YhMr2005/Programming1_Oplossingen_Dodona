# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/763446685

def geldige_zet(schaakzet):
    if len(schaakzet) not in (2, 3):
        return False

    if not schaakzet[-1] in '12345678':
        return False
    if not schaakzet[-2].isalpha() or not schaakzet[-2].islower():
        return False
    if len(schaakzet) == 3:
        if not schaakzet[0] in 'KDTLP':
            return False

    return True

def geldige_zetten(schaakzetten):
    for zet in schaakzetten:
        if not geldige_zet(zet): # Is equivalent met: if geldige_zet(zet) == False
            return False
    return True
