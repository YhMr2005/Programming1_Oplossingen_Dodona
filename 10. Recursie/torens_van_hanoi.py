# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1092659960

def hanoi(n, start='A', tijdelijk='B', einde='C', outer_loop=False):
    counter = 0
    if n == 1:
        print(f"Schijf {n} van {start} naar {einde}")
        if not outer_loop: # Is equivalent met: if outer_loop is False
            print("1 stappen gedaan")
            return
        return 1

    counter = hanoi(n-1, start, einde, tijdelijk, True)
    counter += 1
    print(f"Schijf {n} van {start} naar {einde}")
    counter += hanoi(n-1, tijdelijk, start, einde, True)
    
    if not outer_loop: # Is equivalent met: if outer_loop is False
        print(f"{counter} stappen gedaan")
        return
    return counter