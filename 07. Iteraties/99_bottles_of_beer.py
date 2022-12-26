# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1317066143

getal = int(input())

while getal > 2:
    print(getal, "flesjes met bier op de muur,", getal, "flesjes met bier.")
    print("Open er een, drink hem meteen,", getal-1, "flesjes met bier op de muur.")
    getal -= 1

print("2 flesjes met bier op de muur, 2 flesjes met bier.")
print("Open er een, drink hem meteen, 1 flesje met bier op de muur.")

print("1 flesje met bier op de muur, 1 flesje met bier.")
print("Open er een, drink hem meteen, 0 flesjes met bier op de muur.")
 