# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/623087135

def nieuw_kaartspel(kleuren_arr, waarden_arr):
    kaartspel = []
    for kleur in kleuren_arr:
        for waarde in waarden_arr:
            kaartspel.append(kleur+waarde)
    return kaartspel

def splits_kaartspel(kaartspel_arr):
    return (kaartspel_arr[:len(kaartspel_arr)//2], kaartspel_arr[len(kaartspel_arr)//2:])
    
def faro_shuffle(kaartspel1, kaartspel2):
    kaartspel_output = []
    for i in range(min(len(kaartspel1), len(kaartspel2))):
        kaartspel_output.extend([kaartspel1[i], kaartspel2[i]])
    if len(kaartspel2) > len(kaartspel1):
        kaartspel_output.append(kaartspel2[-1])
    return kaartspel_output