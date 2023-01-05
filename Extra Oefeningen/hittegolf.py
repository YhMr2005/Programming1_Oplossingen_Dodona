from copy import copy

aantal_gevallen = int(input())

testgevallen = []
for i in range(aantal_gevallen):
    temperaturen = []
    nieuwe_temp = input()
    while nieuwe_temp != 'stop':
        temperaturen.append(float(nieuwe_temp))
        nieuwe_temp = input()
    testgevallen.append(temperaturen)

for index, geval in enumerate(testgevallen):
    hittegolf = False
    geval_kopie = copy(geval)
    geval_opgesplitst = []
    volgnummer_tijdelijk = 0
    while len(geval_kopie) > 0:
        for i, temperatuur in enumerate(geval_kopie):
            volgnummer_tijdelijk += 1
            if temperatuur < 25:
                geval_opgesplitst.append((volgnummer_tijdelijk-len(geval_kopie[:i]), geval_kopie[:i]))
                geval_kopie = geval_kopie[i+1:]
                break
    for deel_van_geval in geval_opgesplitst:
        if len(deel_van_geval[1]) >= 5 and len([x for x in deel_van_geval[1] if x >= 30]) >= 3:
            hittegolf = True
            volgnummer = deel_van_geval[0]
            print(index+1, volgnummer, len(deel_van_geval[1]))
            break
    if hittegolf is False:
        print(index+1, "geen hittegolf")
    hittegolf = False
