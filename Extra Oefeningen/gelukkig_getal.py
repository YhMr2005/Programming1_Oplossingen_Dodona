invoer = int(input("Geef een strikt positief geheel getal in: "))
while invoer <= 0:
    invoer = int(input("Geef een positief geheel getal in: "))

getal = invoer
while True:
    cijfers = [cijfer for cijfer in str(getal)]
    getal = sum([int(cijfer)**2 for cijfer in cijfers])
    if getal == 1:
        print(invoer, "is gelukkig")
        break
    if getal == 4:
        print(invoer, "is ongelukkig")
        break
