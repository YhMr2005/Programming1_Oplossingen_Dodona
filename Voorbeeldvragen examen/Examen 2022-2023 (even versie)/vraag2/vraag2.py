import random

class Speler:
    def __init__(self, naam, wapen):
        self.naam = naam
        self.wapens = [wapen.lower()]
        self.is_levend = True
        self.aantal_kills = 0
    
    def __str__(self):
        speler_status = "levend" if self.is_levend else "dood"
        wapens_uitvoer = "', '".join(self.wapens)
        lijn1 = f"{self.naam} is {speler_status}\n"
        lijn2 = f"aantal vermoord {self.aantal_kills}\n"
        lijn3 = f"Wapens: '{wapens_uitvoer}'"
        uitvoer = lijn1 + lijn2 + lijn3

        return uitvoer
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.naam == other.naam

    def vermoord(self, andere_speler):
        assert self.is_levend, "U bent dood. U kan dus geen andere speler vermoorden."
        assert andere_speler.is_levend, "De speler die u probeert te vermoorden is al dood."
        assert self != andere_speler, "U kunt niet zichzelf vermoorden."

        self.aantal_kills += 1
        andere_speler.is_levend = False
        overgebleven_wapens = []

        for wapen in andere_speler.wapens:
            # Als het wapen wordt afgepakt van andere_speler, verdwijnt het uit zijn wapens, anders blijf hij ze behouden. 
            if wapen not in self.wapens:
                self.wapens.append(wapen)
            else:
                overgebleven_wapens.append(wapen)
        
        andere_speler.wapens = overgebleven_wapens

        return None

class Gevecht:
    def __init__(self, speler1, speler2):
        assert speler1.is_levend and speler2.is_levend, "De spelers moeten levend zijn."
        self.speler1 = speler1
        self.speler2 = speler2
    
    def vecht(self):
        spelers = [self.speler1, self.speler2]
        winnaar = random.choice(spelers)
        spelers.remove(winnaar)
        verliezer = spelers[0]

        winnaar.vermoord(verliezer)

        return None
