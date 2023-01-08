from demografie import *

stad_leuven = Stad("Leuven", 102000)
stad_duh = Stad("Duh", 5000)
stad_gent = Stad("Gent", 263429)
stad_hasselt = Stad("Hasselt", 80000)
stad_genk = Stad("Genk", 85000)
stad_genk2 = Stad("Genk", 5000)

demografie_vlaanderen = Demografie("Vlaanderen")
demografie_vlaanderen.voeg_stad_toe(stad_leuven)
demografie_vlaanderen.voeg_stad_toe(stad_duh)
demografie_vlaanderen.voeg_stad_toe(stad_gent)
demografie_vlaanderen.voeg_stad_toe(stad_hasselt)
demografie_vlaanderen.voeg_stad_toe(stad_genk)
demografie_vlaanderen.voeg_stad_toe(stad_genk2)

print(demografie_vlaanderen)

demografie_vlaanderen.fusioneer("Gent", "Duh", "GentPlus")

print(demografie_vlaanderen)

demografie_vlaanderen.print_steden_met_minimum_aantal_inwoners(100000)
