# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/601978768

def gast(maand, leeftijd):
    return (maand*2 + 5) * 50 + leeftijd - 365

def macArthur(getal):
    getal += 115
    if len(str(getal)) == 3:
        return (int(str(getal)[0]), int(str(getal)[1:]))
    if len(str(getal)) == 4:
        return (int(str(getal)[:2]), int(str(getal)[2:]))

    # korter: return (int((str(getal+115)[-3::-1])[::-1]), int(str(getal+115)[-2:]))
