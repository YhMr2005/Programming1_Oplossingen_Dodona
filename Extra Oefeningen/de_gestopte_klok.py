# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1477235114

from datetime import datetime

# Vertrek van thuis
dag_thuis = 1
vertrek_thuis_h = int(input())
vertrek_thuis_m = int(input())
vertrek_thuis = datetime(1, 1, dag_thuis, hour=vertrek_thuis_h, minute=vertrek_thuis_m)

# Aankomst bij vriendin
dag_vriendin = 1
aankomst_vriendin_h = int(input())
aankomst_vriendin_m = int(input())
aankomst_vriendin = datetime(1, 1, dag_vriendin, hour=aankomst_vriendin_h, minute=aankomst_vriendin_m)

# Vertrek van vriendin
vertrek_vriendin_h = int(input())
vertrek_vriendin_m = int(input())
vertrek_vriendin = datetime(1, 1, dag_vriendin, hour=vertrek_vriendin_h, minute=vertrek_vriendin_m)
if vertrek_vriendin_h < aankomst_vriendin_h:
    dag_vriendin += 1
    vertrek_vriendin = datetime(1, 1, dag_vriendin, hour=vertrek_vriendin_h, minute=vertrek_vriendin_m)

# Aankomst thuis
aankomst_thuis_h = int(input())
aankomst_thuis_m = int(input())
aankomst_thuis = datetime(1, 1, dag_thuis, hour=aankomst_thuis_h, minute=aankomst_thuis_m)
if aankomst_thuis_h < vertrek_thuis_h:
    dag_thuis += 1
    aankomst_thuis = datetime(1, 1, dag_thuis, hour=aankomst_thuis_h, minute=aankomst_thuis_m)

# Berekeningen
volledige_trip_duur = (aankomst_thuis - vertrek_thuis)
bij_vriendin_duur = (vertrek_vriendin - aankomst_vriendin)
huidige_tijd = vertrek_vriendin + ((volledige_trip_duur - bij_vriendin_duur) / 2)

# Uitvoer
print(huidige_tijd.hour)
print(huidige_tijd.minute)
