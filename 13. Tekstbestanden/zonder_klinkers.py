# https://dodona.ugent.be/nl/courses/1286/series/14357/activities/1551924012

def zonder_klinkers(bestand_lezen, bestand_schrijven):
    origineel = open(bestand_lezen)
    kopie = open(bestand_schrijven, 'w')

    klinkers = 'aeiou'
    ingelezen_chars = 0
    geschreven_chars = 0

    for char in origineel.read():
        ingelezen_chars += 1
        if char.lower() not in klinkers:
            kopie.write(char)
            geschreven_chars += 1

    origineel.close()
    kopie.close()
    return (ingelezen_chars, geschreven_chars)
