# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1952876754

# Oplossing 1:
getal = int(input())
vorig_getal = 0
huidig_getal = 1
# 
print(vorig_getal)
print(huidig_getal)
while huidig_getal <= getal:
    nieuw_getal = huidig_getal + vorig_getal
    vorig_getal = huidig_getal
    huidig_getal = nieuw_getal
    print(huidig_getal)

# Oplossing 2 (veel simpeler):
# getal = int(input())
# a, b = 0, 1
# while a <= getal:
#     print(a)
#     a, b = b, a+b
# print(a) # Het eerstvolgend getal groter dan de invoer