# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/267979422

getallen = [int(input()), int(input()), int(input())]

for i, getal in enumerate(getallen):
    if getallen.count(getal) == 1:
        zwart_schaap = getal
        index = i
        
hoeveelste_getal = {0: 'eerste', 1: 'tweede', 2: 'derde'}
print(f"Het {hoeveelste_getal[index]} getal, nl. {zwart_schaap} is het zwarte schaap.")
