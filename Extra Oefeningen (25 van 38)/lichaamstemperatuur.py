# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/328212300
from math import exp

e = exp(1)
lichaamstemp = float(input())

if 100/lichaamstemp < e-0.1:
    print("je hebt koorts")
elif 100/lichaamstemp > e+0.1:
    print("je bent onderkoeld")
else:
    print("je hebt een normale lichaamstemperatuur")

