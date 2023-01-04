# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/325610135
from math import sqrt

cirkel_1 = {"coordinaat": (float(input()), float(input())), "straal": float(input())}
cirkel_2 = {"coordinaat": (float(input()), float(input())), "straal": float(input())}

def afstand(cirkel1, cirkel2):
    p1 = cirkel1["coordinaat"]
    p2 = cirkel2["coordinaat"]
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def isGelijkAan(getal1, getal2):
    if abs(getal1 - getal2) < 0.000001:
        return True
    else:
        return False

if isGelijkAan(afstand(cirkel_1, cirkel_2), 0):
    print("concentrisch")
elif isGelijkAan(afstand(cirkel_1, cirkel_2), abs(cirkel_1["straal"] - cirkel_2["straal"])):
    print("binnen rakend")
elif isGelijkAan(afstand(cirkel_1, cirkel_2), cirkel_1["straal"] + cirkel_2["straal"]):
    print("buiten rakend")
elif afstand(cirkel_1, cirkel_2) < abs(cirkel_1["straal"] - cirkel_2["straal"]):
    print("omsluitend")
elif afstand(cirkel_1, cirkel_2) > abs(cirkel_1["straal"] - cirkel_2["straal"]) and afstand(cirkel_1, cirkel_2) < cirkel_1["straal"] + cirkel_2["straal"]:
    print("snijdend")
elif afstand(cirkel_1, cirkel_2) > cirkel_1["straal"] + cirkel_2["straal"]:
    print("gescheiden")
