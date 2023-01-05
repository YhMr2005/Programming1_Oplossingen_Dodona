# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/779259935

def hoogtemeters(lijst_hoogtes):
    hoogteverschillen = []
    for i in range(len(lijst_hoogtes)-1):
        hoogteverschillen.append(lijst_hoogtes[i+1]-lijst_hoogtes[i])
    return hoogteverschillen

def dalen_en_stijgen(hoogteverschillen):
    # Kan ook met list-comprehension, bv. stijgen = sum([x for x in hoogteverschillen if x > 0])
    dalen = abs(sum(filter(lambda x: x < 0, hoogteverschillen)))
    stijgen = sum(filter(lambda x: x > 0, hoogteverschillen))
    return (dalen, stijgen)
