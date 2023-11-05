# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/373633979

# Oplossing 1: zonder gebruik van set
lijst = [1, 3, 7,  2, 5, 6, 3, 8, 5, 7, 6, 1]

nieuwe_lijst = []
for num in lijst:
    if num not in nieuwe_lijst:
        nieuwe_lijst.append(num)

nieuwe_lijst.sort()

print(nieuwe_lijst)

# Oplossing 2: met gebruik van set
# lijst = [1, 3, 7,  2, 5, 6, 3, 8, 5, 7, 6, 1]
# print(sorted(list(set(lijst))))
print(lijst)
