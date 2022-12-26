# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/954463058

woord = input()

uitvoer = ""

i = 0
while i < len(woord):
    if woord[i] == "[":
        start = i+1
        j = i+1
        while woord[j] != "]":
            j += 1
        einde = j
        uitvoer += woord[start:einde]
    i += 1

print(uitvoer)
