class Verkeerslicht:
    def __init__(self, toestand="rood"):
        assert toestand in ("groen", "oranje", "rood"), "Geen geldige toestand"
        self.toestand = toestand

    def __str__(self):
        return self.toestand
    
    def __repr__(self):
        return f"Verkeerslicht('{self.toestand}')"
    
    def volgende(self):
        volgende_toestand = {
            "rood": "groen",
            "groen": "oranje",
            "oranje": "rood"
        }
        nieuwe_toestand = volgende_toestand[self.toestand]
        self.toestand = nieuwe_toestand
