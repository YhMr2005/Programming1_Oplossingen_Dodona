# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/2030651884

class Stad:
    def __init__(self, naam_stad, inwoners_aantal=5000):
        if isinstance(inwoners_aantal, int) and inwoners_aantal >= 70:
            self.naam = naam_stad
            self.inwoners_aantal = inwoners_aantal

    def __repr__(self):
        return f"{self.naam} heeft {self.inwoners_aantal} inwoners"

    def __eq__ (self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.naam == other.naam
    
    def heeft_meer_inwoners(self, other):
        return self.inwoners_aantal > other.inwoners_aantal


class Demografie:
    def __init__(self, naam_regio):
        self.naam = naam_regio
        self.steden = []
    
    def __repr__(self):
        uitvoer = f"Regio: {self.naam}\nTotaal aantal inwoners: {self.bereken_totaal_aantal_inwoners()}"
        for stad in self.steden:
            uitvoer += f"\n{stad.__repr__()}"
        return uitvoer
    
    def voeg_stad_toe(self, nieuwe_stad):
        if nieuwe_stad not in self.steden:
            self.steden.append(nieuwe_stad)
            self.steden.sort(key=lambda x: x.inwoners_aantal)
    
    def bereken_totaal_aantal_inwoners(self):
        totaal_inwoners = 0
        for stad in self.steden:
            totaal_inwoners += stad.inwoners_aantal
        return totaal_inwoners
    
    def fusioneer(self, stad1_naam, stad2_naam, nieuwe_naam):
        inwoners1 = 0
        inwoners2 = 0
        for stad in self.steden:
            if stad.naam == stad1_naam:
                stad1 = stad
                inwoners1 = stad1.inwoners_aantal
            if stad.naam == stad2_naam:
                stad2 = stad
                inwoners2 = stad2.inwoners_aantal
        nieuwe_stad = Stad(nieuwe_naam, inwoners1 + inwoners2)
        self.steden.remove(stad1)
        self.steden.remove(stad2)
        self.voeg_stad_toe(nieuwe_stad)
    
    def geef_steden_met_minimum_aantal_inwoners(self, min_inwoners):
        return [stad for stad in self.steden if stad.inwoners_aantal >= min_inwoners]
    
    def print_steden_met_minimum_aantal_inwoners(self, min_inwoners):
        uitvoer_steden = self.geef_steden_met_minimum_aantal_inwoners(min_inwoners)
        print(f"steden met meer dan dan {min_inwoners} inwoners:")
        for stad in uitvoer_steden:
            print(stad)
