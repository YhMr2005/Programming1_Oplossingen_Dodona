# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/2096226599

class BankRekening:
    def __init__(self, rek_naam, rek_nummer, bedrag=0):
        self.naam = rek_naam
        self.nummer = rek_nummer
        self.bedrag = bedrag
    
    def __str__(self):
        return "{}, {}, bedrag: {}".format(self.naam, self.nummer, self.bedrag)

    def __repr__(self):
        return "BankRekening('{}', '{}', {})".format(self.naam, self.nummer, self.bedrag)

    def storten(self, n):
        self.bedrag += n

    def afhalen(self, n):
        self.bedrag -= n

