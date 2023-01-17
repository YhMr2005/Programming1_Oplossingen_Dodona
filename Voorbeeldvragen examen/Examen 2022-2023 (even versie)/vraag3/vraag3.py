data = open("input.txt", 'r', encoding="latin-1")
uitvoer = open("totale_tijd.csv", 'w', encoding="latin-1")

wielrenners = {}

while True:
    nieuwe_lijn = data.readline()
    if nieuwe_lijn == '':
        break
    
    data_lijn = nieuwe_lijn.split(",")
    if "\n" in data_lijn[-1]:
        data_lijn[-1] = data_lijn[-1].replace("\n", "")

    volledige_naam = data_lijn[0] + ";" + data_lijn[1]
    tijd = int(data_lijn[-1])

    if volledige_naam not in wielrenners:
        wielrenners[volledige_naam] = tijd
    else:
        wielrenners[volledige_naam] += tijd

for wielrenner in wielrenners:
    uitvoer.write(wielrenner + ";" + str(wielrenners[wielrenner]) + "\n")

data.close()
uitvoer.close()
