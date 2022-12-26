# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1567511933

def afvlakken(inttuple, uitvoer=None):
    if uitvoer is None:
        uitvoer = tuple()
        
    for element in inttuple:
        if isinstance(element, int):
            uitvoer += (element,)
        elif isinstance(element, tuple):
            uitvoer = afvlakken(element, uitvoer)
    return uitvoer
