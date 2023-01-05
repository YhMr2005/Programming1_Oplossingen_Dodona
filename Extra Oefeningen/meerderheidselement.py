# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/326318244

def meerderheid(lijst):
    for getal in lijst:
        if lijst.count(getal) > len(lijst)/2:
            return getal
    return -1
