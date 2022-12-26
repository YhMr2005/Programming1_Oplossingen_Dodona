# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1159766268

# Oplossing 1: zonder gebruik van sets
woord1 = str(input())
woord2 = str(input())

gemeenschappelijk = ""

for character in woord2:
    if character in woord1 and character not in gemeenschappelijk:
        gemeenschappelijk += character

print(gemeenschappelijk)

# Oplossing 2: met gebruik van sets
# woord1 = set(input())
# woord2 = set(input())
# print(''.join(woord1.intersection(woord2)))
