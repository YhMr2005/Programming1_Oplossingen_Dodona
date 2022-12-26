# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/1273258863

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


