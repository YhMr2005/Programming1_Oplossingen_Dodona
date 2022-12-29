# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1797346540

start_uur = int(input())
start_min = int(input())
eind_uur = int(input())
eind_min = int(input())
start_decimaal = float(str(start_uur)+str(start_min/60)[1:])
eind_decimaal = float(str(eind_uur)+str(eind_min/60)[1:])

if start_uur not in range(18, 24) or eind_uur not in range(18, 24) or eind_uur < start_uur:
    print("ongeldige invoer")

else:
    if start_decimaal >= 18 and start_decimaal <= 21.5:
        if eind_decimaal <= 21.5:
            bedrag =  2*(eind_decimaal - start_decimaal)
        else:
            bedrag = 2*(21.5 - start_decimaal) + 4*(eind_decimaal - 21.5)
    else:
        bedrag = 4*(eind_decimaal - start_decimaal)

    print(bedrag)
