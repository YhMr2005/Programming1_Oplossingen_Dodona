# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/1204583816

alles = {'Socrates', 'Plato', 'Eratosthenes', 'Zeus', 'Hera', 'Athene', 'Acropolis', 'Kat', 'Hond'}
mensen = {'Socrates', 'Plato', 'Eratosthenes'}
sterfelijken = {'Socrates', 'Plato', 'Eratosthenes', 'Kat', 'Hond'}

A = alles.intersection(mensen).issubset(sterfelijken)
B = 'Socrates' in mensen # Of: {'Socrates'}.issubset(mensen)
C = 'Socrates' in sterfelijken # Of: {'Socrates'}.issubset(sterfelijken)
D = len(sterfelijken.difference(mensen)) > 0
E = len(alles.difference(sterfelijken)) > 0
