# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/2045812829

class Kleur:
    def __init__(self, r=0, g=0, b=0):
        if r < 0:
            r = 0
        if g < 0:
            g = 0
        if b < 0:
            b = 0
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return "({}, {}, {})".format(self.r, self.g, self.b)


    def invers(self):
        return Kleur(255-self.r, 255-self.g, 255-self.b)

    def grijswaarde(self):
        grijswaarde = int(0.3*self.r + 0.59*self.g + 0.11*self.b)
        return Kleur(grijswaarde, grijswaarde, grijswaarde)