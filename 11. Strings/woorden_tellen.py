# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/2032693594

# Oplossing 1:
woord = input()
zin = input()
aantal = 0

while zin.count(woord) != 0:
    start = zin.find(woord)
    if zin[start-1].isalpha() or zin[start+len(woord)].isalpha():
        # Het woord is onderdeel van een ander woord
        zin = zin.replace(woord, "", 1)
    else:
        aantal += 1
        zin = zin.replace(woord, "", 1)

print(f"Aantal keren dat het woord \"{woord}\" voorkomt: {aantal}")

# Oplossing 2:
# woord = input()
# zin = input()
# 
# for char in zin: # Verwijder leestekens
    # if not char.isalpha() and char != ' ':
        # zin = zin.replace(char, '')
# 
# zin_lijst = zin.split()
# 
# print(f"Aantal keren dat het woord \"{woord}\" voorkomt: {zin_lijst.count(woord)}")