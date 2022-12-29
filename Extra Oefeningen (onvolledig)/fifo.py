# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1273258863

arr = []
woord = input()

while woord != 'STOP':
    if woord == '?':
        if len(arr) > 0:
            print(arr.pop(0))
        woord = input()
    else:
        arr.append(woord)
        woord = input()
