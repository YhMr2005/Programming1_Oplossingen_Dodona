maand, dag = int(input()), int(input())

maanden_31_dagen = [1, 3, 5, 7, 8, 10, 12]

if maand == 2 and dag == 28:
    volgende_maand = True
elif maand in maanden_31_dagen and dag == 31:
    volgende_maand = True
elif maand not in maanden_31_dagen and dag == 30:
    volgende_maand = True
else:
    volgende_maand = False

if volgende_maand:
    nieuwe_dag = 1
    nieuwe_maand = maand + 1
    if nieuwe_maand > 12:
        nieuwe_maand = 1
else:
    nieuwe_dag = dag + 1
    nieuwe_maand = maand

print(nieuwe_maand)
print(nieuwe_dag)
