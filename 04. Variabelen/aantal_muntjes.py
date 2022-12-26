# https://dodona.ugent.be/nl/courses/1286/series/14345/activities/715315832

# bedrag (in cent)
bedrag = 1156

dollars = bedrag // 100
kwartjes = (bedrag % 100) // 25
dubbeltes = (bedrag % 25) // 10
stuivers = (bedrag % 10) // 5
centen = (bedrag % 5)

print("Dollars:", dollars)
print("Kwartjes:", kwartjes)
print("Dubbeltjes:", dubbeltes)
print("Stuivers:", stuivers)
print("Centen:", centen)
