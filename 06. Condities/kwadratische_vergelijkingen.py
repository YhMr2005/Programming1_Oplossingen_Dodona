# https://dodona.ugent.be/nl/courses/1286/series/14347/activities/1886347387

a = int(input())
b = int(input())
c = int(input())
discriminant = b**2 - 4*a*c
if a == b == 0:
    print("Ongeldige vergelijking")
elif a == 0:
    print("Er is 1 reële oplossing:", -c/b)
elif discriminant == 0:
    print("Er is 1 reële oplossing:", (-b + discriminant**0.5)/(2*a))
elif discriminant > 0:
    print("Er zijn 2 reële oplossingen:", (-b - discriminant**0.5)/(2*a), "en", (-b + discriminant**0.5)/(2*a))
elif discriminant < 0:
    print("Er zijn geen reële oplossingen")
