# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1150748783

from random import random
from math import sqrt

n = int(input())
m = 0

for i in range(n):
    x_coordinaat = random()
    y_coordinaat = random()
    if sqrt(x_coordinaat**2 + y_coordinaat**2) <= 1:
        m += 1 

print((4*m)/n)
