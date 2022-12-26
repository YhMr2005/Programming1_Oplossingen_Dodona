# https://dodona.ugent.be/nl/courses/1286/series/14358/activities/2128064180

numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int(input("Give an index: "))
except ValueError:
    print("Fout: De opgegeven waarde moet een geheel getal zijn.")

else:
    try:
        print("100 /", numlist[i1], "=", 100 / numlist[i1])
    except IndexError:
        print(f"Fout: De index moet liggen tussen {-len(numlist)} en {len(numlist)-1}.")
    except ZeroDivisionError:
        print("Fout: Kan niet delen door 0. Het element in de lijst met de gekozen index heeft waarde 0.")
    except TypeError:
        print("Fout: Het element in de lijst met opgegeven index is geen getal.")