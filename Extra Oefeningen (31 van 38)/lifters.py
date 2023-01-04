# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1432498809
from math import ceil
from sys import exit

aantal_lifters = int(input())

eerste_helft = []
tweede_helft = []

for i in range(aantal_lifters // 2):
    eerste_helft.append(float(input()))
for i in range(ceil(aantal_lifters/2)):
    tweede_helft.append(float(input()))

for index, score in enumerate(tweede_helft):
    if score > max(eerste_helft):
        print(score)
        exit()
    elif index == len(tweede_helft)-1:
        print(score)
