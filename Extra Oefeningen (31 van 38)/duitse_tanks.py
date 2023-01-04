# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1100982831

serienummmers = []

nummer = int(input())
while nummer >= 0:
    serienummmers.append(nummer)
    nummer = int(input())
    
geschat = round((((len(serienummmers)+1) * max(serienummmers)) / len(serienummmers)) - 1)

print(f"Het aantal geproduceerde tanks wordt geschat op {geschat}.")
