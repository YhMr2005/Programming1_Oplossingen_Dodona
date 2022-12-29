# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/101669433

def combisom(lijst, som):
    for i in range(len(lijst)):
        for j in range(len(lijst)):
            if  i != j and lijst[i] + lijst[j] == som:
                return True
    return False
    