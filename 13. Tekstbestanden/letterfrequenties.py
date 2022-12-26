# https://dodona.ugent.be/nl/courses/1286/series/14357/activities/14378608

def letterfrequenties(bestand_1, bestand_2, bestand_3, bestand_4):
    ALFABET = 'abcdefghijklmnopqrstuvwxyz'
    schrijf_bestand = open(bestand_4, 'w')
    
    for letter in ALFABET:
        frequentie_1 = berekenFrequentie(letter, bestand_1)
        frequentie_2 = berekenFrequentie(letter, bestand_2)
        frequentie_3 = berekenFrequentie(letter, bestand_3)
        schrijf_bestand.write(f"{letter},{frequentie_1:.5f},{frequentie_2:.5f},{frequentie_3:.5f}\n")

    schrijf_bestand.close()
    return

def berekenFrequentie(letter, bestand):
    """
    Berekent frequentie van een bepaalde letter in een bepaald tekstbestand.
    """
    tekst = open(bestand).read()
    totaal_aantal_tekens = 0
    aantal_voorkomen = 0

    for char in tekst:
        if char.isalpha():
            totaal_aantal_tekens += 1
        if char.lower() == letter:
            aantal_voorkomen += 1

    frequentie = aantal_voorkomen / totaal_aantal_tekens
    return frequentie
