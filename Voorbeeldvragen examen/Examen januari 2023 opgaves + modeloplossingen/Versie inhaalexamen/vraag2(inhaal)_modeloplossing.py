class Mijn:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.geraakt = False

    def is_geraakt(self):
        return self.geraakt

    def raak(self):
        self.geraakt = True

    def __eq__(self, andere_mijn: object) -> bool:
        if not isinstance(andere_mijn,Mijn):
            return False
        return andere_mijn.x == self.x and andere_mijn.y == self.y
    

class Veld:
    def __init__(self, hoogte, mijnen = []) -> None:
        assert hoogte in range(3,6), "hoogte van het veld moet minimaal 3 en maximaal 5 zijn"
        for m in mijnen:
            assert mijnen.count(m) == 1, "element mag maar 1 keer voorkomen"
            assert m.x in range(1,hoogte+1) and m.y in range(1,hoogte+1), "mijnen moeten in veld liggen"
        self.hoogte = hoogte
        self.mijnen = mijnen


    def raak_mijn(self,x,y):
        if Mijn(x,y) in self.mijnen:
            self.mijnen.remove(Mijn(x,y))
            nieuwe_mijn = Mijn(x,y)
            nieuwe_mijn.raak()
            self.mijnen.append(nieuwe_mijn)
    
    def __repr__(self):
        uit = ""
        for i in range(1,self.hoogte+1):
            lijn = ""
            for j in range(1,self.hoogte+1):
                lijn += "."
            for m in self.mijnen:
                if m.x == i and m.is_geraakt():
                    lijn= lijn[:(m.y-1)] + "X" + lijn[m.y:]
            uit+= lijn + "\n"
        return uit


mijnen = [Mijn(1,2),Mijn(1,4),Mijn(2,2),Mijn(3,4)]
v = Veld(4,mijnen)
v.raak_mijn(2,2)
v.raak_mijn(3,4)
v.raak_mijn(1,1)
print(v)