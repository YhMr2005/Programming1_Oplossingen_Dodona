getallen = input()
lijst = getallen.split()
lijst = list(map(int, lijst)) # Strings omzetten naar integers
uitvoer = []

for i in range(1, len(lijst)-1):
    if lijst[i] > lijst[i-1] and lijst[i] > lijst[i+1]:
        uitvoer.append(i)

print(uitvoer)
