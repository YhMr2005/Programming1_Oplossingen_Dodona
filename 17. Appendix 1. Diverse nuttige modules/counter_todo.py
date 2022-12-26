# https://dodona.ugent.be/nl/courses/1286/series/14368/activities/1266518248

from collections import Counter

tekst = input()
print(Counter(tekst.replace(" ", "")).most_common(5))
