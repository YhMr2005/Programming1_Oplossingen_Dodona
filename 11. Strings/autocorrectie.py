# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/804070970

zin = input()
zin_arr = zin.split()

# 1
nieuwe_arr = []
for woord in zin_arr:
    if woord[0].isupper() and woord[1].isupper() and woord[2].islower():
        woord = woord[0] + woord[1].lower() + woord[2:]
    nieuwe_arr.append(woord)
zin = " ".join(nieuwe_arr)
zin_arr = zin.split()

# 2
nieuwe_arr = []
vorig = ""
for woord in zin_arr:
    if woord == vorig:
        zin_arr.remove(woord)
    vorig = woord
zin = " ".join(zin_arr)
zin_arr = zin.split()

# 3
if zin[0].islower():
    zin = zin.replace(zin[0], zin[0].upper())
zin_arr = zin.split()

# 4
nieuwe_arr = []
for woord in zin_arr:
    if woord[0].islower() and woord[1:].isupper():
        woord = woord[0].upper() + woord[1:].lower()
    nieuwe_arr.append(woord)
    
zin = " ".join(nieuwe_arr)
zin_arr = zin.split()

# 5
dagen = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
for dag in dagen:
    if dag in zin:
        zin = zin.replace(dag, dag.title())
    
print(zin)