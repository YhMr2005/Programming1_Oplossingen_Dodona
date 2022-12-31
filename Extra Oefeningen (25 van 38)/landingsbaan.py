# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1954949630

hoek = float(input())

# aanduiding 1
aanduiding1 = int(round(hoek, -1)/10)

# 0 -> 36
if aanduiding1 == 0:
    aanduiding1 = 36

# aanduiding 2
if aanduiding1 <= 18:
    aanduiding2 = aanduiding1 + 18
else:
    aanduiding2 = aanduiding1 - 18

# aanduiding1 is kleinste
if aanduiding2 < aanduiding1:
    aanduiding1, aanduiding2 = aanduiding2, aanduiding1

# print
print(f"{aanduiding1:02d}/{aanduiding2}")
