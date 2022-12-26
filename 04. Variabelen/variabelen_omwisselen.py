# https://dodona.ugent.be/nl/courses/1286/series/14345/activities/1865001586

# twee waarden toekennen aan twee variabelen
a = 17
b = 23

# waarde toegekend aan variabelen uitschrijven
print(f'a = {a} en b = {b}')

# waarden van variabelen omwisselen
a += b
# voeg hier twee regels toe om a en b om te wisselen
b = a - b
a -= b
# waarde toegekend aan variabelen uitschrijven
print(f'a = {a} en b = {b}')

"""
Deze opdracht kan veel eenvoudiger opgelost worden:
# waarden van variabelen omwisselen
a, b = b, a
"""