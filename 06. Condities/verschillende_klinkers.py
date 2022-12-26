# https://dodona.ugent.be/nl/courses/1286/series/14347/activities/1014821966


zin = input()

counter = 0

for i in 'aeiou':
    if i in zin.lower():
        counter += 1


if counter == 0:
    print("De zin bevat geen klinkers.")
elif counter == 1:
    print("De zin bevat slechts 1 verschillende klinker.")

else:
    print('De zin bevat', counter, 'verschillende klinkers.')