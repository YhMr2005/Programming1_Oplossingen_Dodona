# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1294363212

def vlag(richting, kleuren):
    uitvoer = ''
    if richting == 'verticaal':
        for kleur in kleuren:
            uitvoer += kleur + ' | '
        return uitvoer[:-3] # Verwijder laatste streep en spaties
    elif richting == 'horizontaal':
        for kleur in kleuren:
            uitvoer += kleur + '\n-\n'
        return uitvoer[:-3] # Verwijder laatste streepje en newlines 
