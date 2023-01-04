# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1325500143

def samenvoegen(arr1, arr2):
    lijst_1 = list(arr1)
    lijst_2 = list(arr2)
    uitvoer = []
    for i in range(min(len(lijst_1), len(lijst_2))):
        uitvoer.append(lijst_1[i])
        uitvoer.append(lijst_2[i])

    return uitvoer

def weven(arr1, arr2):
    '''
    Waarschijnlijk kan dit veel eenvoudiger en eleganter opgelost worden,
    maar onderstaande code werkt en ik heb geen zin om er verder over na te denken.
    '''
    lijst_1 = list(arr1)
    lijst_2 = list(arr2)
    uitvoer = []
    for i in range(max(len(lijst_1), len(lijst_2))):
        if i > len(lijst_1)-1:
            if len(lijst_1) == 1:
                j = 0
            else:
                j = i - (len(lijst_1))
                while j > len(lijst_1)-1:
                    j -= len(lijst_1)
        else:
            j = i
        uitvoer.append(lijst_1[j])

        if i > len(lijst_2)-1:
            if len(lijst_2) == 1:
                j = 0
            else:
                j = i - (len(lijst_2))
                while j > len(lijst_2)-1:
                    j -= len(lijst_2)
        else:
            j = i
        uitvoer.append(lijst_2[j])
    
    return uitvoer

def ritsen(arr1, arr2):
    lijst_1 = list(arr1)
    lijst_2 = list(arr2)
    uitvoer = []
    for i in range(min(len(lijst_1), len(lijst_2))):
        uitvoer.append(lijst_1[i])
        uitvoer.append(lijst_2[i])
    for i in range(max(len(lijst_1), len(lijst_2)) - min(len(lijst_1), len(lijst_2))):
        uitvoer.append(max(lijst_1, lijst_2, key=len)[len(min(lijst_1, lijst_2, key=len))+i])

    return uitvoer
