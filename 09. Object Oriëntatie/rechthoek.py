# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/1773014461

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

    def overlap(self, rechthoek):
        r1, r2 = self , rechthoek
        if self.punt.x > rechthoek.punt.x or (self.punt.x == rechthoek.punt.x and self.punt.y > rechthoek.punt.y):
            r1, r2 = rechthoek, self
        if r1.rechtsonder().x <= r2.punt.x or r1.rechtsonder().y <= r2.punt.y:
            return None
        return Rechthoek( r2.punt, min( r1.rechtsonder().x - r2.punt.x, r2.breedte ), min( r1.rechtsonder().y - r2.punt.y, r2.hoogte ))