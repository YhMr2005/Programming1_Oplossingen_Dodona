# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/879249671

# Oplossing 1:
getal = int(input())

som = 0
veelvoud = getal

while veelvoud <= 100:
    som += veelvoud
    veelvoud += getal

print(som)

# Oplossing 2: met gebruik van list comprehension
# getal = int(input())
# print(sum([i for i in range(101) if i % getal == 0]))
