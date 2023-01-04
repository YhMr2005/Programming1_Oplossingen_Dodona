# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1303919335

populatie = float(input())
vruchtbaarheid = float(input())
aantal_tijdsstappen = int(input())

for i in range(aantal_tijdsstappen):
    print(populatie)
    populatie = vruchtbaarheid*populatie*(1-populatie)
