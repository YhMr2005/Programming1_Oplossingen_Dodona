# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/582245450

def fruitstuk_toevoegen(mand, fruit):
    for element in mand:
        if len(fruit) == len(element):
            mand.remove(element)
            mand.append(fruit)
    if fruit not in mand:
        mand.append(fruit)
    mand.sort(key=lambda x: len(x))
    return mand

def maak_fruitmand(fruit_arr):
    fruitmand = []
    for fruit in fruit_arr:
        for element in fruitmand:
            if len(fruit) == len(element):
                fruitmand.remove(element)
                fruitmand.append(fruit)
        if fruit not in fruitmand:
            fruitmand.append(fruit)
    fruitmand.sort(key=lambda x: len(x))
    return fruitmand