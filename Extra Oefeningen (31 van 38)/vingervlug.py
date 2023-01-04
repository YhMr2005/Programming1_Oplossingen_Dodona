# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1199472779

getal1 = int(input())
getal2 = int(input())

if (getal1 <= 5 and getal2 <= 5) or 10 in (getal1, getal2):
    print(f"{getal1} x {getal2} = {getal1*getal2}")

elif getal1 in range(6, 10) and getal2 in range(6, 10):
    print(f"{getal1} x {getal2} = 10 x ({abs(getal1-5)} + {abs(getal2-5)}) + ({abs(getal1-10)} x {abs(getal2-10)}) = {getal1*getal2}")

elif getal1 in range(11, 16) and getal2 in range(11, 16):
    print(f"{getal1} x {getal2} = 100 + 10 x ({getal1-10} + {getal2-10}) + ({getal1-10} x {getal2-10}) = {getal1*getal2}")

else:
    print(f"{getal1} x {getal2} = 100 + 10 x ({getal1-10} + {getal2-10}) + ({getal1-10} x {getal2-10}) = {getal1*getal2}")
