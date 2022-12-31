# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1235806490

allel_1 = input()
allel_2 = input()

abo = allel_1 + allel_2

# match-case is nieuw sinds Python 3.10. Onderstaande kan ook met if-else statements.
match abo:
    case 'AA':
        res = 'A'
    case 'AB' | 'BA':
        res = 'AB'
    case 'AO' | 'OA':
        res = 'A'
    case 'BB':
        res = 'B'
    case 'BO' | 'OB':
        res = 'B'
    case 'OO':
        res = 'O'

print(f"De combinatie van de ABO allelen {allel_1} en {allel_2} resulteert in bloedgroep {res}.")
