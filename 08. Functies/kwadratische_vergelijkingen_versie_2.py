# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/446763531
from math import sqrt


def discriminant(a, b, c):
    var = b**2-4*a*c
    return float("{:.1f}".format(var))

def oplossingen(a, b, c):
    if discriminant(a,b,c) < 0:
        aantal_opl = 0
        x1, x2 = 0, 0
    elif discriminant(a,b,c) == 0:
        aantal_opl = 1
        x1, x2 = -b/(2*a), -b/(2*a)
    else:
        aantal_opl = 2
        x1 = (-b - sqrt(discriminant(a,b,c)))/(2*a)
        x2 = (-b + sqrt(discriminant(a,b,c)))/(2*a)
    
    return (aantal_opl, x1, x2)
    
