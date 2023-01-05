# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/2038783829

def iszigzag(arr):
    for i in range(0, len(arr), 2):
        if (i-1 >= 0 and arr[i] < arr[i-1]) or (i+1 <= len(arr)-1 and arr[i] < arr[i+1]):
            return False
    return True

def zigzag_traag(lijst):
    lijst.sort()
    for i in range(0, len(lijst), 2):
        if i+1 <= len(lijst)-1 and lijst[i] == lijst[i+1]:
            continue
        if i+1 <= len(lijst)-1:
            lijst[i], lijst[i+1] = lijst[i+1], lijst[i]

    return None

def zigzag_snel(lijst):
    for i in range(0, len(lijst), 2):
        if i-1 >= 0 and lijst[i] < lijst[i-1]:
            lijst[i], lijst[i-1] = lijst[i-1], lijst[i]
        if i+1 <= len(lijst)-1 and lijst[i] < lijst[i+1]:
            lijst[i], lijst[i+1] = lijst[i+1], lijst[i]

    return None

