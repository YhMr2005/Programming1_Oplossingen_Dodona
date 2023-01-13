class ISBN13:
    def __init__(self, getal, lengte_landaanduiding=1):
        assert lengte_landaanduiding in range(1, 6), "ongeldige ISBN code"
        self.code = getal
        self.lengte_landaanduiding = lengte_landaanduiding

    def __str__(self):
        code_str = str(self.code)
        prefix = code_str[:3]
        landaanduiding = code_str[3:self.lengte_landaanduiding+3]
        identificatienummer = code_str[self.lengte_landaanduiding+3:12]
        controlenummer = code_str[12]
        return f"{prefix}-{landaanduiding}-{identificatienummer}-{controlenummer}"

    def __repr__(self):
        return f"ISBN13({self.code}, {self.lengte_landaanduiding})"
    
    def isgeldig(self):
        if isinstance(self.code, int) and len(str(self.code)) == 13:
            code_str = str(self.code)
            controle_o = int(code_str[0]) + int(code_str[2]) + int(code_str[4]) + int(code_str[6]) + int(code_str[8]) + int(code_str[10])
            controle_e = int(code_str[1]) + int(code_str[3]) + int(code_str[5]) + int(code_str[7]) + int(code_str[9]) + int(code_str[11])
            controle_cijfer = (10 - (controle_o + 3*controle_e) % 10) % 10

            if int(code_str[12]) == controle_cijfer:
                return True

        return False 
    
    def alsISBN10(self):
        code_str = str(self.code)
        if not self.isgeldig() or not code_str.startswith("978"):
            return None
        
        isbn10_zonder_controle = code_str[3:-1]
        controle_cijfer = (int(isbn10_zonder_controle[0]) + 2*int(isbn10_zonder_controle[1]) + 3*int(isbn10_zonder_controle[2]) + 4*int(isbn10_zonder_controle[3]) + 5*int(isbn10_zonder_controle[4]) + 6*int(isbn10_zonder_controle[5]) + 7*int(isbn10_zonder_controle[6]) + 8*int(isbn10_zonder_controle[7]) + 9*int(isbn10_zonder_controle[8])) % 11

        if controle_cijfer == 10:
            controle_cijfer = "X"

        isbn10_code = f"{isbn10_zonder_controle[:self.lengte_landaanduiding]}-{isbn10_zonder_controle[self.lengte_landaanduiding:]}-{controle_cijfer}"
        
        return isbn10_code
