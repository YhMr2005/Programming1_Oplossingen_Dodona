from copy import copy

def verwissel(lijst, i):
    originele_lijst = copy(lijst)
    for i in range(i, len(lijst)-1):
        if lijst[i] > lijst[i+1]:
            lijst[i], lijst[i+1] = lijst[i+1], lijst[i]

    if lijst != originele_lijst:
        return True
    else:
        return False


def sorteer(lijst):
    for i in range(len(lijst)):
        response = verwissel(lijst, i)
        if response is False:
            break

    return None
