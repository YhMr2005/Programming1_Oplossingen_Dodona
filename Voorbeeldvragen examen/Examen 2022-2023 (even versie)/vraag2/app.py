from vraag2 import *

thor = Speler("Thor", "Stormbreaker")
thanos = Speler("Thanos", "Infinity Stones")

print(thor)
print(thanos)
print("------------------")
thor_vs_thanos = Gevecht(thor, thanos)
thor_vs_thanos.vecht()
print(thor)
print(thanos)
