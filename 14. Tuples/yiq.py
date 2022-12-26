# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/2097740983

def yiq(rgb_kleur):
    y = 0.299*rgb_kleur[0] + 0.587*rgb_kleur[1] + 0.114*rgb_kleur[2]
    i = 0.596*rgb_kleur[0] - 0.274*rgb_kleur[1] - 0.322*rgb_kleur[2]
    q = 0.211*rgb_kleur[0] - 0.523*rgb_kleur[1] + 0.312*rgb_kleur[2]
    yiq_kleur = (round(y, 4), round(i, 4), round(q, 4))
    return yiq_kleur
    