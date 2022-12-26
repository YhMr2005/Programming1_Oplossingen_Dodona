# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/2008047746

import random

simulatie = 200000
start = 'A'
som_levensduur = 0

huidige_levensduur = 0
vorige_plaats = ''
nu_plaats = start
nieuwe_plaats = ''

for i in range(simulatie):
    while nu_plaats != 'D':
        huidige_levensduur += 1
        if not vorige_plaats:
            nieuwe_plaats = random.choice('BCD')
            vorige_plaats = nu_plaats
            nu_plaats = nieuwe_plaats

        else:
            beschikbare_keuze = 'ABCD'
            beschikbare_keuze = beschikbare_keuze.replace(nu_plaats, '')
            beschikbare_keuze = beschikbare_keuze.replace(vorige_plaats, '')
            nieuwe_plaats = random.choice(beschikbare_keuze)
            vorige_plaats = nu_plaats
            nu_plaats = nieuwe_plaats

    som_levensduur += huidige_levensduur
    huidige_levensduur = 0
    vorige_plaats = ''
    nu_plaats = start
    nieuwe_plaats = ''

gem_levensduur = som_levensduur / simulatie

print('{:.2f}'.format(gem_levensduur))

