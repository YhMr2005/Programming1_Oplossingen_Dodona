# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/1773014461

"""
Opmerking i.v.m. de overlap()-methode in klasse Rechthoek:

Ik denk dat Dodona hierbij niet klopt. De onderstaande code in overlap() is volgens mij
fout, maar wordt wel goedgekeurd door Dodona.
Eronder staat in commentaar de code waarvan ik denk dat het juist is,
maar volgens Dodona geeft het een fout resultaat, terwijl als je de rechthoeken
uittekent, je zal zien dat het wél juist is!
"""

class Punt:
    def __init__(self, x, y):
        assert type(x), type(y) is int
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Punt({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.x == other.x and self.y == other.y

class Rechthoek:
    def __init__(self, punt_lb, breedte, hoogte):
        assert type(breedte), type(hoogte) is int
        assert breedte > 0 and hoogte > 0, "ongeldige rechthoek"
        self.punt = punt_lb
        self.punt_x, self.punt_y = punt_lb.x, punt_lb.y
        self.breedte = breedte
        self.hoogte = hoogte
    
    def __repr__(self):
        return "Rechthoek({}, {}, {})".format(self.punt, self.breedte, self.hoogte)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.punt == other.punt and self.breedte == other.breedte and self.hoogte == other.hoogte

    def oppervlakte(self):
        return self.breedte*self.hoogte

    def omtrek(self):
        return 2*(self.breedte + self.hoogte)

    def rechtsonder(self):
        return Punt(self.punt_x + self.breedte, self.punt_y + self.hoogte)

    """
    LET OP: Deze code voor overlap() is volgens mij fout, maar wordt wel goedgekeurd
    door Dodona. Onderaan in commentaar staat de code die volgens mij wel juist is.
    """
    def overlap(self, rechthoek):
        r1, r2 = self, rechthoek
        if r1.punt_x > r2.punt_x or (r1.punt_x == r2.punt_x and r1.punt_y > r2.punt_y):
            r1, r2 = r2, r1
        if r1.rechtsonder().x <= r2.punt_x or r1.rechtsonder().y <= r2.punt_y:
            return None
        return Rechthoek(r2.punt, min(r1.rechtsonder().x-r2.punt_x, r2.breedte), min(r1.rechtsonder().y-r2.punt_y, r2.hoogte))

    """
    Onderstaande code voor overlap() is in mijn ogen correct, maar wordt niet goedgekeurd door Dodona.
    Als je de rechthoeken uittekent, zul je zien dat dit echter wél de juiste oplossing geeft.
    """
    # def overlap(self, rechthoek):
    #     if r1.punt_x > r2.punt_x: # zorg dat r1 altijd de meest linkse rechthoek is
    #         r1, r2 = r2, r1

    #     if r1.punt_y <= r2.punt_y: # r1 ligt boven r2
    #         if r1.rechtsonder().x <= r2.punt_x or r1.rechtsonder().y <= r2.punt_y: # geen overlapping
    #             return None
    #         else: # wel overlapping
    #             return Rechthoek(r2.punt, min(r1.rechtsonder().x-r2.punt.x, r2.breedte), min(r1.rechtsonder().y-r2.punt.y, r2.hoogte))
    #     else: # r1 ligt onder r2
    #         if r1.rechtsonder().x <= r2.punt_x or r2.rechtsonder().y <= r1.punt_y: # geen overlap
    #             return None
    #         else: # wel overlapping
    #             return Rechthoek(Punt(r2.punt_x, r1.punt_y), min(r1.rechtsonder().x-r2.punt.x, r2.breedte), min(r2.rechtsonder().y-r1.punt.y, r1.hoogte))
