# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/1269944782

personen = []
for i in range(4):
    personen.append(int(input()))
personen.sort()

totale_tijd = personen[0] + 3*personen[1] + personen[3]

if totale_tijd < 60:
    print(f"De snelste tijd om over te steken is {totale_tijd} minuten")
else:
    print(f"De snelste tijd om over te steken is {totale_tijd // 60} uur en {totale_tijd % 60} minuten")