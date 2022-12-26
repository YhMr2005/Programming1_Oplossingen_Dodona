# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/818523397

def behoort_tot_taal(woord, taal):
    if len(woord) < 1:
        return False
    for letter in woord:
        if letter not in taal.union({' '}):
            return False
    return True

def is_onleesbaar(woord, taal):
    for letter in woord:
        if letter in taal.union({' '}):
            return False
    return True

def perfect_woord(woord, taal):
    for letter in taal:
        if letter not in woord: 
            return False
    return True
    