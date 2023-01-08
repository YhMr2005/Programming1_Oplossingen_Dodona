# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1092659960

def hanoi(n, start='A', tijdelijk='B', einde='C', outer_loop=True):
    counter = 0
    if n == 1:
        print(f"Schijf {n} van {start} naar {einde}")
        if outer_loop:
            print("1 stappen gedaan")
            return
        return 1

    counter = hanoi(n-1, start, einde, tijdelijk, False)
    counter += 1
    print(f"Schijf {n} van {start} naar {einde}")
    counter += hanoi(n-1, tijdelijk, start, einde, False)
    
    if outer_loop:
        print(f"{counter} stappen gedaan")
        return
    return counter
