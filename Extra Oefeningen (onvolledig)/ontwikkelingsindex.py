# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/554093539

from math import sqrt, log

land = input()
le = float(input())
mys = float(input())
eys = float(input())
gni = float(input())

lei = (le-20) / (82.3-20)
ei = sqrt((mys/13.2) * (eys/20.6)) / 0.951
ii = (log(gni)-log(100)) / (log(107721) - log(100))

hdi = (lei * ei * ii) ** (1/3)

print(f"De HDI van {land} bedraagt {hdi:.3f}.")
